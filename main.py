import logging
from DiscordBot import DiscordBot
import discord
import os

DISCORD_BOT_TOKEN = os.getenv("DISCORD_BOT_TOKEN")

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(module)s - %(funcName)s - %(lineno)d - %(message)s",
    handlers=[logging.FileHandler("bot.log"), logging.StreamHandler()],
)
intents = discord.Intents.default()
intents.guilds = True
bot = DiscordBot(command_prefix="!", intents=intents)
bot.run(DISCORD_BOT_TOKEN)
