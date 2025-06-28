import discord
from utils.autorole_roles import load_roles, save_roles
from utils.language_database import languages
from utils.settings_store import get_language

class RoleAssignView(discord.ui.View):
    def __init__(self, cog, rank):
        super().__init__(timeout=120)
        self.cog = cog
        self.rank = rank
        self.add_item(self.RoleDropdown(self))

    class RoleDropdown(discord.ui.RoleSelect):
        def __init__(self, parent):
            self.parent = parent
            super().__init__(
                placeholder="Wähle eine Rolle aus...",
                min_values=1,
                max_values=1,
                custom_id="role_select"
            )

        async def callback(self, interaction: discord.Interaction):
            guild_id = str(interaction.guild.id)
            data = load_roles()
            if guild_id not in data:
                data[guild_id] = {}
            data[guild_id][self.parent.rank] = self.values[0].id
            save_roles(data)

            # ✅ Lokaler Import hier – zur Vermeidung von Circular Import
            from views.rank_select import RankSelectView

            await interaction.response.edit_message(
                embed=self.parent.cog.build_settings_embed(interaction.guild),
                view=RankSelectView(self.parent.cog)
            )
