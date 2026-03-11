import discord
from discord.ext import commands
import os
import json
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv("DISCORD_TOKEN")

CONFIG_PATH = "config.json"
with open(CONFIG_PATH, "r") as f:
    config = json.load(f)

TARGET_GUILD_ID = config.get("verify_server_id")
if not TARGET_GUILD_ID:
    raise ValueError("verify_server_id must be set in config.json for single-server usage.")

intents = discord.Intents.default()
intents.message_content = True
intents.members = True

class MyBot(commands.Bot):
    def __init__(self):
        super().__init__(command_prefix="!", intents=intents)

    async def setup_hook(self):
        # Liste deiner Cogs
        initial_extensions = [
            "cogs.link",
            "cogs.stats",
            "cogs.info",
            "cogs.game",
            "cogs.leaderboard",
            "cogs.autoroles"
        ]
        for ext in initial_extensions:
            await self.load_extension(ext)

        guild_obj = discord.Object(id=TARGET_GUILD_ID)

        # Slash Commands nur im Ziel-Server synchronisieren
        await self.tree.sync(guild=guild_obj)
        print(f"✅ Slash commands synced for guild {TARGET_GUILD_ID}.")

bot = MyBot()

@bot.event
async def on_ready():
    print(f"✅ Logged in as {bot.user} (ID: {bot.user.id})")

bot.run(TOKEN)
