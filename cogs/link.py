import discord
from discord.ext import commands
from discord import app_commands
import random
import string
import time
import json
import os
from datetime import datetime

from utils.image_reader import extract_text_from_image
from utils.db import link_account, get_linked_account, load_db, save_db
from utils.verify_store import store_code, check_code, verify_cache
from utils.settings_store import get_language
from utils.language_database import languages
from utils.val_api import authorized_client

CACHE_PATH = "data/mmr_cache.json"
os.makedirs("data", exist_ok=True)

def load_cache():
    if not os.path.exists(CACHE_PATH):
        return {}
    with open(CACHE_PATH, "r") as f:
        return json.load(f)

def save_cache(data):
    with open(CACHE_PATH, "w") as f:
        json.dump(data, f, indent=2)

class Link(commands.GroupCog, name="link"):
    def __init__(self, bot):
        self.bot = bot

    @app_commands.command(name="add", description="Start or complete your VALORANT account verification")
    async def add(self, interaction: discord.Interaction, screenshot: discord.Attachment = None):
        lang = get_language(interaction.guild.id)
        await interaction.response.defer(ephemeral=True)

        user_id = interaction.user.id

        if screenshot:
            image_bytes = await screenshot.read()
            text = extract_text_from_image(image_bytes)
            result = check_code(user_id, text)

            if result["success"]:
                tagline = result["tagline"]
                link_account(user_id, tagline)
                verify_cache.pop(str(user_id), None)

                # MMR-Cache Update starten
                name, tag = tagline.split("#")
                url = f"https://api.henrikdev.xyz/valorant/v1/mmr/eu/{name}/{tag}"
                async with authorized_client() as session:
                    res = await session.get(url)
                    if res.status_code == 200:
                        data = await res.json()
                        mmr = data.get("data", {})
                        cache = load_cache()
                        cache[str(user_id)] = {
                            "riot_tagline": tagline,
                            "rank": mmr.get("currenttierpatched", "Unknown"),
                            "rank_icon": mmr.get("images", {}).get("small", ""),
                            "rr": mmr.get("ranking_in_tier", 0),
                            "kd": mmr.get("kd_ratio", 0),
                            "hs_percent": mmr.get("headshot_percent", 0),
                            "invisible": False,
                            "updated_at": datetime.utcnow().isoformat()
                        }
                        save_cache(cache)

                response_text = languages["link"]["verification_success"][lang].replace("{tagline}", tagline)
                await interaction.followup.send(response_text, ephemeral=True)
            else:
                await interaction.followup.send(languages["link"]["verification_failed"][lang], ephemeral=True)
        else:
            verify_cache.pop(str(user_id), None)

            # Generate unique 6-digit code
            existing_codes = {
                v["code"] for v in verify_cache.values()
                if time.time() - v["created_at"] <= 600
            }
            code = ''.join(random.choices(string.ascii_uppercase + string.digits, k=6))
            while (
                sum(c.isalpha() for c in code) < 2 or
                sum(c.isdigit() for c in code) < 2 or
                code in existing_codes
            ):
                code = ''.join(random.choices(string.ascii_uppercase + string.digits, k=6))

            embed = discord.Embed(
                title="VALORANT Account Verification",
                description=f"**`{code}`**\n\n{languages['link']['verification_started'][lang]}",
                color=discord.Color.purple()
            )
            embed.set_footer(text="Only you can see this message. Expires in 10 minutes")

            await interaction.followup.send(embed=embed, ephemeral=True)
            store_code(user_id, code, thread=None)

    @app_commands.command(name="get", description="Show your currently linked VALORANT account")
    async def get(self, interaction: discord.Interaction):
        lang = get_language(interaction.guild.id)
        await interaction.response.defer(ephemeral=True)

        user_id = interaction.user.id
        linked = get_linked_account(user_id)

        if linked:
            tagline = linked.get("riot_tagline")
            embed = discord.Embed(
                title=languages["link"]["linked_account_info"][lang].replace("{tagline}", tagline),
                color=discord.Color.green()
            )
        else:
            embed = discord.Embed(
                title=languages["link"]["no_link_found"][lang],
                color=discord.Color.red()
            )

        await interaction.followup.send(embed=embed, ephemeral=True)

    @app_commands.command(name="remove", description="Remove your linked VALORANT account")
    async def remove(self, interaction: discord.Interaction):
        lang = get_language(interaction.guild.id)
        await interaction.response.defer(ephemeral=True)

        user_id = str(interaction.user.id)
        db = load_db()

        if user_id in db:
            del db[user_id]
            save_db(db)
            await interaction.followup.send(languages["link"]["link_removed"][lang], ephemeral=True)
        else:
            await interaction.followup.send(languages["link"]["no_link_found"][lang], ephemeral=True)

async def setup(bot: commands.Bot):
    await bot.add_cog(Link(bot))
