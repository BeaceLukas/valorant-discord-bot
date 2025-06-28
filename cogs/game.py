# cogs/game.py

import discord
from discord.ext import commands
from discord import app_commands
from utils.db import get_linked_account
from utils.settings_store import get_language
from utils.language_database import languages
from utils.val_api import authorized_client

class Game(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @app_commands.command(name="game", description="Show your last 10 ranked VALORANT matches")
    @app_commands.describe(tagline="Optional: name#tag")
    async def game(self, interaction: discord.Interaction, tagline: str = None):
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

        url = f"https://api.henrikdev.xyz/valorant/v1/lifetime/matches/eu/{name}/{tag}?mode=competitive"
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
                await interaction.followup.send(languages["game"]["no_data"][lang], ephemeral=True)
                return

        embed = discord.Embed(
            title=languages["game"]["title"][lang].replace("{tagline}", f"{name}#{tag}"),
            color=discord.Color.from_rgb(25, 25, 25)
        )

        guild_emojis = {e.name: str(e) for e in interaction.guild.emojis}

        for match in data[:10]:
            meta = match.get("meta", {})
            stats = match.get("stats", {})

            agent = meta.get("agent", "Unknown")
            emoji = guild_emojis.get(agent, "")

            kills = stats.get("kills", 0)
            deaths = stats.get("deaths", 1)
            assists = stats.get("assists", 0)
            headshots = stats.get("headshots", 0)
            bodyshots = stats.get("bodyshots", 0)
            legshots = stats.get("legshots", 0)

            kd = round(kills / deaths, 2)
            hs_total = headshots + bodyshots + legshots
            hs_percent = round((headshots / hs_total) * 100, 1) if hs_total > 0 else 0

            line = (
                f"{emoji} {agent}\n"
                f"{languages['game']['kda'][lang]}: {kills}/{deaths}/{assists}\n"
                f"{languages['game']['kd'][lang]}: {kd} | {languages['game']['hs'][lang]}: {hs_percent}%"
            )
            embed.add_field(name="​", value=line, inline=False)

        await interaction.followup.send(embed=embed)

async def setup(bot: commands.Bot):
    await bot.add_cog(Game(bot))
