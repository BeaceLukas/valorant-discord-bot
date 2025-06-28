# cogs/stats.py

import discord
from discord.ext import commands
from discord import app_commands
from utils.db import get_linked_account
from utils.settings_store import get_language
from utils.language_database import languages
from utils.val_api import authorized_client
import json

class Stats(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @app_commands.command(name="stats", description="Show your current VALORANT rank")
    @app_commands.describe(tagline="Optional: name#tag")
    async def stats(self, interaction: discord.Interaction, tagline: str = None):
        lang = get_language(interaction.guild.id)
        await interaction.response.defer(ephemeral=False)

        if not tagline:
            linked = get_linked_account(interaction.user.id)
            if not linked:
                await interaction.followup.send(languages["errors"]["no_account"][lang], ephemeral=True)
                return
            tagline = linked.get("riot_tagline")

        try:
            name, tag = tagline.split("#")
        except ValueError:
            await interaction.followup.send(languages["errors"]["invalid_tagline"][lang], ephemeral=True)
            return

        url = f"https://api.henrikdev.xyz/valorant/v1/mmr/eu/{name}/{tag}"
        async with authorized_client() as session:
            res = await session.get(url)
            if res.status_code == 429:
                await interaction.followup.send(languages["errors"]["rate_limited"][lang], ephemeral=True)
                return
            if res.status_code != 200:
                await interaction.followup.send(languages["errors"]["api_down"][lang], ephemeral=True)
                return

            data = (await res.json()).get("data")
            if not data:
                await interaction.followup.send(languages["errors"]["no_account"][lang], ephemeral=True)
                return

        embed = discord.Embed(
            title=languages["stats"]["title"][lang].replace("{tagline}", f"{name}#{tag}"),
            color=discord.Color.from_rgb(25, 25, 25)
        )
        embed.set_thumbnail(url=data.get("images", {}).get("small", ""))
        embed.add_field(name=languages["stats"]["rank"][lang], value=data.get("currenttierpatched", "-"), inline=True)
        embed.add_field(name=languages["stats"]["mmr_change"][lang], value=str(data.get("mmr_change_to_last_game", "-")), inline=True)

        await interaction.followup.send(embed=embed)

async def setup(bot: commands.Bot):
    await bot.add_cog(Stats(bot))
