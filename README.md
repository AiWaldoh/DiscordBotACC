# Discord Event Notification Bot

This is a Discord bot that sends notifications for upcoming events in a specified guild. It is built using the discord.py library and utilizes Python's Poetry dependency management.

## Prerequisites

- Python 3.10 or higher
- Poetry (Python dependency management)

## Installation

1. Clone the repository:
   git clone https://github.com/AiWaldoh/DiscordBotACC.git

2. Change into the project directory:
   cd DiscordBotACC

3. Install the dependencies using Poetry:
   poetry install

4. Create a `.env` file in the project root and add the following variables:
   DISCORD_BOT_TOKEN=your_bot_token
   NOTIFICATION_CHANNEL_ID=your_notification_channel_id
   NOTIFICATION_GUILD_ID=your_notification_guild_id
   NOTIFICATION_HOURS=1,24

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
- `.env`: Environment variables file for storing sensitive information.
- `pyproject.toml`: Poetry configuration file.
- `poetry.lock`: Lock file generated by Poetry to ensure consistent dependencies.
- `requirements.txt`: File containing the project dependencies (generated by Poetry).

## Contributing

Contributions are welcome! If you find any issues or have suggestions for improvements, please open an issue or submit a pull request.

## License

This project is licensed under the [MIT License](LICENSE).