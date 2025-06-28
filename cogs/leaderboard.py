# cogs/leaderboard.py

import discord
from discord.ext import commands
from discord import app_commands
import json
import os
from utils.settings_store import get_language
from utils.language_database import languages

CACHE_PATH = "data/mmr_cache.json"

class Leaderboard(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @app_commands.command(name="leaderboard", description="Show server VALORANT leaderboard")
    async def leaderboard(self, interaction: discord.Interaction):
        lang = get_language(interaction.guild.id)
        await interaction.response.defer()

        if not os.path.exists(CACHE_PATH):
            await interaction.followup.send(languages["leaderboard"]["not_enough_data"][lang], ephemeral=True)
            return

        with open(CACHE_PATH, "r") as f:
            cache = json.load(f)

        if not cache:
            await interaction.followup.send(languages["leaderboard"]["not_enough_data"][lang], ephemeral=True)
            return

        entries = []
        for user_id, info in cache.items():
            member = interaction.guild.get_member(int(user_id))
            rank = info.get("rank", "Unknown")
            rr = info.get("rr", 0)
            kd = round(info.get("kd", 0), 2)
            hs = round(info.get("hs_percent", 0))
            invisible = info.get("invisible", False)
            tagline = info.get("riot_tagline", "?")

            rank_emoji_name = rank.replace(" ", "_")
            emoji = discord.utils.get(interaction.guild.emojis, name=rank_emoji_name)
            emoji_display = f"{emoji} " if emoji else ""

            visible = not invisible or interaction.user.guild_permissions.administrator

            entry = {
                "user_id": user_id,
                "sort_rank": rank,
                "rr": rr,
                "kd": kd,
                "hs": hs,
                "emoji": emoji_display,
                "tagline": tagline if visible else languages["leaderboard"]["anonymous"][lang],
                "mention": member.mention if member and visible else "",
                "invisible": invisible,
                "original_rank": info.get("rank", "")
            }
            entries.append(entry)

        # Sortierung: Rank, RR, KD
        entries.sort(key=lambda e: (e["sort_rank"], e["rr"], e["kd"]), reverse=True)

        embed = discord.Embed(
            title=languages["leaderboard"]["title"][lang],
            color=discord.Color.from_rgb(25, 25, 25)
        )

        requester_id = str(interaction.user.id)
        requester_rank = None

        for index, entry in enumerate(entries[:10], start=1):
            name = f"{index}. {entry['emoji']}{entry['original_rank']} {entry['rr']} RR"
            line = f"**{entry['tagline']}** / {entry['mention']}" if entry["user_id"] == requester_id else f"{entry['tagline']} / {entry['mention']}"
            stats = f"      KD: {entry['kd']} | HS: {entry['hs']}%"
            embed.add_field(name=name, value=f"{line}{stats}", inline=False)

        for i, entry in enumerate(entries):
            if entry["user_id"] == requester_id:
                if i >= 10:
                    name = f"**X. {entry['emoji']}{entry['original_rank']} {entry['rr']} RR**"
                    line = f"**{entry['tagline']}** / {entry['mention']}"
                    stats = f"      KD: {entry['kd']} | HS: {entry['hs']}%"
                    embed.add_field(name=name, value=f"{line}{stats}", inline=False)
                break

        await interaction.followup.send(embed=embed)

async def setup(bot: commands.Bot):
    await bot.add_cog(Leaderboard(bot))
