import discord
from discord.ext import commands, tasks
from datetime import datetime, timedelta
import pytz
from dotenv import load_dotenv
import os
import logging

load_dotenv()

NOTIFICATION_GUILD_ID = int(os.getenv("NOTIFICATION_GUILD_ID"))
NOTIFICATION_CHANNEL_ID = int(os.getenv("NOTIFICATION_CHANNEL_ID"))
NOTIFICATION_HOURS = [int(hour) for hour in os.getenv("NOTIFICATION_HOURS").split(",")]


class DiscordBot(commands.Bot):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.timezone = pytz.timezone("Canada/Atlantic")
        self.events = []

    # override on_ready from subclass (commands.Bot) to initialize app
    async def on_ready(self):
        logging.info(f"Logged in as {self.user.name}")
        self.load_events.start()
        self.check_event_times.start()

    # check for newly created events every 30 minutes from discord server
    @tasks.loop(minutes=30)
    async def load_events(self):
        guild = self.get_guild(NOTIFICATION_GUILD_ID)
        if guild:
            try:
                self.events = await guild.fetch_scheduled_events()
                logging.info(
                    f"Loaded {len(self.events)} events from guild: {guild.name}"
                )
            except Exception as e:
                logging.error(f"Error loading events: {str(e)}")

    # every minute, check if there's an upcoming event
    @tasks.loop(minutes=1)
    async def check_event_times(self):
        channel = self.get_channel(NOTIFICATION_CHANNEL_ID)

        if channel:
            current_time = datetime.now(self.timezone)
            for event in self.events:
                event_start_time = event.start_time.astimezone(self.timezone)
                time_diff = event_start_time - current_time

                for notification_hour in NOTIFICATION_HOURS:
                    notification_time = timedelta(hours=notification_hour)
                    if (
                        notification_time
                        < time_diff
                        <= notification_time + timedelta(minutes=1)
                    ):
                        footer_message = f"Starts in {notification_hour} hour{'s' if notification_hour > 1 else ''}"
                        embed = self.create_event_message(event, footer_message)
                        await channel.send(embed=embed)
                        logging.info(f"Sent notification for event: {event.name}")

    # create and format a message for the event
    @staticmethod
    def create_event_message(event, footer_message):
        if not isinstance(event, discord.ScheduledEvent):
            return None

        embed = discord.Embed(
            title=event.name, description=event.description, color=discord.Color.blue()
        )
        if event.creator:
            embed.set_author(name=event.creator.name, icon_url=event.creator.avatar.url)

        if event.cover_image:
            embed.set_thumbnail(url=event.cover_image)

        embed.set_footer(text=footer_message)
        return embed
