# cogs/autoroles.py

import discord
from discord.ext import commands
from discord import app_commands

from views.autorole_main import AutoRoleMainView
from utils.settings_store import get_language
from utils.language_database import languages


class AutoRoles(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @app_commands.command(name="autorole", description="Konfiguriere das AutoRole System für VALORANT Ränge")
    @app_commands.checks.has_permissions(administrator=True)
    async def autorole(self, interaction: discord.Interaction):
        lang = get_language(interaction.guild.id)
        embed = discord.Embed(
            title="AutoRole Verwaltung",
            description=languages["autoroles"]["setup_instruction"][lang],
            color=discord.Color.purple()
        )
        await interaction.response.send_message(embed=embed, view=AutoRoleMainView(), ephemeral=True)


async def setup(bot: commands.Bot):
    await bot.add_cog(AutoRoles(bot))
