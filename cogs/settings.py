# cogs/settings.py

import discord
from discord.ext import commands
from discord import app_commands

from utils.settings_store import set_language, get_language
from utils.language_database import languages

class Settings(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @app_commands.command(name="settings", description="Change bot settings (Admin only)")
    @app_commands.default_permissions(administrator=True)
    @app_commands.checks.has_permissions(administrator=True)
    @app_commands.describe(language="Select the bot language")
    @app_commands.choices(language=[
        app_commands.Choice(name="English 🇬🇧", value="en"),
        app_commands.Choice(name="Deutsch 🇩🇪", value="de")
    ])
    async def settings(self, interaction: discord.Interaction, language: app_commands.Choice[str]):
        guild_id = interaction.guild.id
        set_language(guild_id, language.value)

        # Bestätigungsnachricht aus Sprachdatenbank holen
        lang = language.value
        confirm_text = languages["settings"]["language_updated"][lang]
        await interaction.response.send_message(confirm_text, ephemeral=True)

    @settings.error
    async def settings_error(self, interaction: discord.Interaction, error):
        if isinstance(error, app_commands.MissingPermissions):
            guild_id = interaction.guild.id
            lang = get_language(guild_id) or "en"
            error_text = languages["settings"]["only_admin"][lang]
            await interaction.response.send_message(error_text, ephemeral=True)
        else:
            raise error

async def setup(bot: commands.Bot):
    await bot.add_cog(Settings(bot))
