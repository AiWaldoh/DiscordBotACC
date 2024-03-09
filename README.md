# Discord Event Notification Bot

This is a Discord bot that sends notifications for upcoming events in a specified guild. It is built using the discord.py library and utilizes Python's Poetry dependency management. It checks for new events every 30 minutes and sends a notification. Railway.app costs 5$ a month and can automatically deploys the bot from github.

## Prerequisites

- Python 3.10 or higher
- Poetry (Python dependency management)

## Discord Developer Portal Setup

Before deploying the bot, you need to set up your application in the Discord Developer Portal:

1. Go to the Discord Developer Portal and create a new application. Name it "Events Notifier".
2. Create a description for the Discord bot's profile and save the changes.
3. In the Bot tab, click on "Reset Token" to generate a new bot token. Copy the token and add it to the .env file (instructions below).
4. Remove the public bot permissions and save the changes.
5. In the OAuth2 tab, select "bot" under "Scopes". Then, under Bot Permissions, select "Send Messages", "Read Messages/View Channels" under Text Permissions, and "Manage Events" under General Permissions.
6. Copy the generated URL and open it in your browser. Select the server where you want the bot to join.
7. You may also need to enable developer Mode in Advanced options from your personal discord account in order to copy the Guild (server) and Channel ID from the discord client.


## Installation

1. Clone the repository:
   ```git clone https://github.com/AiWaldoh/DiscordBotACC.git```

2. Change into the project directory:
   ```cd DiscordBotACC```

3. Install poetry
   ```sudo apt install python3-poetry```

4. Install the dependencies using Poetry:
   ```poetry install```

5. Rename `.env.example` to `.env` in the project root and add the values for the following static variables:
   ```
   DISCORD_BOT_TOKEN=your_bot_token
   NOTIFICATION_CHANNEL_ID=your_notification_channel_id
   NOTIFICATION_GUILD_ID=your_notification_guild_id
   NOTIFICATION_HOURS=1,24
   ```

   Replace `your_bot_token` with your actual Discord bot token, `your_notification_channel_id` with the ID of the channel where you want the event notifications to be sent, `your_notification_guild_id` with the ID of the guild from which to fetch the scheduled events, and `NOTIFICATION_HOURS` with a comma-separated list of hours before the event start time when notifications should be sent.

## Usage

To run the bot, use the following command:
poetry run python main.py

The bot will start and connect to the specified Discord guild. It will load the scheduled events from the guild and send notifications to the designated channel based on the configured notification hours.

## Configuration

The bot's behavior can be configured through the following environment variables in the `.env` file:

- `DISCORD_BOT_TOKEN`: The token of your Discord bot.
- `NOTIFICATION_CHANNEL_ID`: The ID of the channel where event notifications will be sent.
- `NOTIFICATION_GUILD_ID`: The ID of the guild from which to fetch the scheduled events.
- `NOTIFICATION_HOURS`: A comma-separated list of hours before the event start time when notifications should be sent (e.g., `1,24`).

## Project Structure

- `main.py`: The main entry point of the bot.
- `DiscordBot.py`: The class definition for the Discord bot.
- `.env`: Environment variables file for storing sensitive information. rename .env.example to .env to have example file.
- `pyproject.toml`: Poetry configuration file.
- `poetry.lock`: Lock file generated by Poetry to ensure consistent dependencies.
- `requirements.txt`: File containing the project dependencies (generated by Poetry).

## Contributing

Contributions are welcome! If you find any issues or have suggestions for improvements, please open an issue or submit a pull request.

## License

This project is licensed under the [MIT License](LICENSE).