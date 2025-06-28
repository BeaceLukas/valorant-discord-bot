import discord
from discord.ext import commands
import os
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv("DISCORD_TOKEN")

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
            "cogs.settings",
            "cogs.autoroles"
        ]
        for ext in initial_extensions:
            await self.load_extension(ext)

        # Slash Commands synchronisieren (global)
        await self.tree.sync()
        print("✅ Slash commands synced.")

bot = MyBot()

@bot.event
async def on_ready():
    print(f"✅ Logged in as {bot.user} (ID: {bot.user.id})")

bot.run(TOKEN)
