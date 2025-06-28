import discord
from utils.db import get_linked_account, load_db, save_db
from utils.val_api import authorized_client
from utils.autorole_roles import load_roles
from utils.mmr_cache import load_cache, save_cache
from utils.settings_store import get_language
from utils.language_database import languages

class AutoRoleUserView(discord.ui.View):
    def __init__(self, cog):
        super().__init__(timeout=None)
        self.cog = cog

    @discord.ui.button(label="Add", style=discord.ButtonStyle.success)
    async def add(self, interaction: discord.Interaction, button: discord.ui.Button):
        lang = get_language(interaction.guild.id)
        await interaction.response.send_message(languages["autoroles"]["start_verification"][lang], ephemeral=True)

    @discord.ui.button(label="Update", style=discord.ButtonStyle.primary)
    async def update(self, interaction: discord.Interaction, button: discord.ui.Button):
        lang = get_language(interaction.guild.id)
        linked = get_linked_account(interaction.user.id)
        if not linked:
            await interaction.response.send_message(languages["autoroles"]["no_account"][lang], ephemeral=True)
            return

        name, tag = linked["riot_tagline"].split("#")
        url = f"https://api.henrikdev.xyz/valorant/v1/mmr/eu/{name}/{tag}"
        async with authorized_client() as session:
            async with session.get(url) as res:
                if res.status != 200:
                    await interaction.response.send_message(languages["errors"]["api_down"][lang], ephemeral=True)
                    return
                data = await res.json()

        current_rank = data.get("data", {}).get("currenttierpatched")
        if not current_rank:
            await interaction.response.send_message(languages["autoroles"]["rank_not_found"][lang], ephemeral=True)
            return

        config = load_roles().get(str(interaction.guild.id), {})
        role_id = config.get(current_rank)
        if not role_id:
            await interaction.response.send_message(
                languages["autoroles"]["no_role_configured"][lang].replace("{rank}", current_rank),
                ephemeral=True
            )
            return

        new_role = interaction.guild.get_role(int(role_id))
        if not new_role:
            await interaction.response.send_message(languages["autoroles"]["role_not_found"][lang], ephemeral=True)
            return

        removed_roles = []
        for rank, rid in config.items():
            role = interaction.guild.get_role(int(rid))
            if role and role in interaction.user.roles and role != new_role:
                await interaction.user.remove_roles(role)
                removed_roles.append(role.name)

        await interaction.user.add_roles(new_role)
        msg = languages["autoroles"]["updated"][lang].replace("{role}", new_role.name)
        if removed_roles:
            msg += "\n" + languages["autoroles"]["removed_roles"][lang].replace("{roles}", ", ".join(removed_roles))

        cache = load_cache()
        uid = str(interaction.user.id)
        if uid in cache:
            cache[uid]["invisible"] = False
            save_cache(cache)

        await interaction.response.send_message(msg, ephemeral=True)

    @discord.ui.button(label="Remove", style=discord.ButtonStyle.danger)
    async def remove(self, interaction: discord.Interaction, button: discord.ui.Button):
        lang = get_language(interaction.guild.id)
        user_id = str(interaction.user.id)
        db = load_db()
        if user_id in db:
            del db[user_id]
            save_db(db)
            await interaction.response.send_message(languages["link"]["link_removed"][lang], ephemeral=True)
        else:
            await interaction.response.send_message(languages["link"]["no_link_found"][lang], ephemeral=True)

    @discord.ui.button(label="Invisibel", style=discord.ButtonStyle.secondary)
    async def invis(self, interaction: discord.Interaction, button: discord.ui.Button):
        lang = get_language(interaction.guild.id)
        config = load_roles().get(str(interaction.guild.id), {})
        removed = 0
        for rank, role_id in config.items():
            role = interaction.guild.get_role(int(role_id))
            if role and role in interaction.user.roles:
                await interaction.user.remove_roles(role)
                removed += 1

        cache = load_cache()
        uid = str(interaction.user.id)
        if uid not in cache:
            cache[uid] = {"riot_tagline": get_linked_account(interaction.user.id)["riot_tagline"], "invisible": True}
        else:
            cache[uid]["invisible"] = True
        save_cache(cache)

        msg = languages["autoroles"]["invisible_success"][lang].replace("{count}", str(removed))
        await interaction.response.send_message(msg, ephemeral=True)
