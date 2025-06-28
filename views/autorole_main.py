import discord
from utils.language_database import languages
from utils.settings_store import get_language
from views.rank_select import RankSelectView
from views.autorole_user import AutoRoleUserView

class AutoRoleMainView(discord.ui.View):
    def __init__(self, cog):
        super().__init__(timeout=None)
        self.cog = cog

    @discord.ui.button(label="Settings", style=discord.ButtonStyle.blurple)
    async def settings(self, interaction: discord.Interaction, button: discord.ui.Button):
        await interaction.response.edit_message(
            embed=self.cog.build_settings_embed(interaction.guild),
            view=RankSelectView(self.cog)
        )

    @discord.ui.button(label="Create Message", style=discord.ButtonStyle.green)
    async def create_message(self, interaction: discord.Interaction, button: discord.ui.Button):
        lang = get_language(interaction.guild.id)
        embed = discord.Embed(
            title="VALORANT Auto Role System",
            description=languages["autoroles"]["user_panel_description"][lang],
            color=discord.Color.purple()
        )
        await interaction.channel.send(embed=embed, view=AutoRoleUserView(self.cog))
        await interaction.response.send_message(languages["autoroles"]["message_created"][lang], ephemeral=True)
