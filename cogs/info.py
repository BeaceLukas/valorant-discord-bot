import discord
from discord.ext import commands
from discord import app_commands

class Info(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @app_commands.command(name="info", description="Zeigt Informationen über den Bot")
    async def info(self, interaction: discord.Interaction):
        embed = discord.Embed(
            title="VALORANT Stats Bot",
            description="Verlinke deinen Riot-Account und zeige deine Statistiken direkt in Discord.",
            color=discord.Color.red()
        )
        embed.add_field(name="Entwickler", value="DeinName#1234", inline=True)
        embed.add_field(name="API", value="[Henrik's API](https://github.com/Henrik-3/unofficial-valorant-api)", inline=True)
        embed.set_footer(text="VALORANT Bot • Powered by Python & discord.py")
        await interaction.response.send_message(embed=embed)

async def setup(bot: commands.Bot):
    await bot.add_cog(Info(bot))
