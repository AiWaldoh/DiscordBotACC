import logging
from DiscordBot import DiscordBot
import discord
import os

try:
    from dotenv import load_dotenv

    load_dotenv()
except ImportError:
    logging.warning(
        "dotenv module not found. Skipping loading of environment variables from .env file."
    )

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(module)s - %(funcName)s - %(lineno)d - %(message)s",
    handlers=[logging.FileHandler("bot.log"), logging.StreamHandler()],
)

DISCORD_BOT_TOKEN = os.getenv("DISCORD_BOT_TOKEN")

if DISCORD_BOT_TOKEN is None:
    logging.error("DISCORD_BOT_TOKEN environment variable is not set.")
    raise ValueError("DISCORD_BOT_TOKEN environment variable is not set.")


intents = discord.Intents.default()
intents.guilds = True
bot = DiscordBot(command_prefix="!", intents=intents)

try:
    bot.run(DISCORD_BOT_TOKEN)
except Exception as e:
    logging.exception("An error occurred while running the bot.")
    raise
