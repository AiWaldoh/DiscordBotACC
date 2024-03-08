import discord
from discord.ext import commands, tasks
from datetime import datetime, timedelta
import pytz
from dotenv import load_dotenv
import os
import logging

load_dotenv()

NOTIFICATION_GUILD_ID = int(os.getenv('NOTIFICATION_GUILD_ID'))
NOTIFICATION_CHANNEL_ID = int(os.getenv('NOTIFICATION_CHANNEL_ID'))
DISCORD_BOT_TOKEN = os.getenv('DISCORD_BOT_TOKEN')
NOTIFICATION_HOURS = [int(hour) for hour in os.getenv('NOTIFICATION_HOURS').split(',')]

intents = discord.Intents.default()
intents.guilds = True

bot = commands.Bot(command_prefix='!', intents=intents)

timezone = pytz.timezone('Canada/Atlantic')

events = []

# logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(module)s - %(funcName)s - %(lineno)d - %(message)s')

def create_event_message(event, footer_message):
    if not isinstance(event, discord.ScheduledEvent):
        return None
    
    embed = discord.Embed(
        title=event.name, 
        description=event.description, 
        color=discord.Color.blue()
    )
    if event.creator:
        embed.set_author(name=event.creator.name, icon_url=event.creator.avatar.url)

    if event.cover_image:
        embed.set_thumbnail(url=event.cover_image)

    embed.set_footer(text=footer_message)
    return embed

@bot.event
async def on_ready():
    logging.info(f'Logged in as {bot.user.name}')
    try:
        load_events.start()
        check_event_times.start()
    except Exception as e:
        logging.error(f'Error starting tasks: {str(e)}')

@tasks.loop(hours=1)
async def load_events():
    global events
    guild = bot.get_guild(NOTIFICATION_GUILD_ID)
    if guild:
        try:
            events = await guild.fetch_scheduled_events()
            logging.info(f'Loaded {len(events)} events from guild: {guild.name}')
        except Exception as e:
            logging.error(f'Error loading events: {str(e)}')

@tasks.loop(minutes=1)
async def check_event_times():
    global events
    channel = bot.get_channel(NOTIFICATION_CHANNEL_ID)

    if channel:
        current_time = datetime.now(timezone)
        for event in events:
            event_start_time = event.start_time.astimezone(timezone)
            time_diff = event_start_time - current_time

            for notification_hour in NOTIFICATION_HOURS:
                notification_time = timedelta(hours=notification_hour)
                if notification_time < time_diff <= notification_time + timedelta(minutes=1):
                    footer_message = f"Starts in {notification_hour} hour{'s' if notification_hour > 1 else ''}"
                    embed = create_event_message(event, footer_message)
                    await channel.send(embed=embed)
                    logging.info(f'Sent notification for event: {event.name}')

# Run the bot
bot.run(DISCORD_BOT_TOKEN)