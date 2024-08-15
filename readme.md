# Bearbot

## Introduction

Bearbot is a Discord bot that utilizes the Pexels API to fetch and display random bear images in a specified Discord channel.

## Requirements

To run Bearbot, you'll need the following:

- Python 3.x
- Pexels API key
- Discord bot token
- Discord channel ID

## Installation

1. Clone the repository: `git clone https://github.com/your-username/Bearbot.git`
2. Navigate to the project directory: `cd Bearbot`
3. Install the required dependencies: `pip install -r requirements.txt`

## Configuration

1. Obtain a Pexels API key by signing up on the [Pexels website](https://www.pexels.com/api/new/).
2. Create a new Discord bot and obtain the bot token. You can follow the official [Discord Developer Portal](https://discord.com/developers/docs/intro) guide for detailed instructions.
3. Find the Discord channel ID where you want Bearbot to send the bear images. You can enable Developer Mode in Discord and right-click on the desired channel to copy its ID.

## Usage

1. Open the `bot.py` file in a text editor.
2. Replace the `PEXELS_API_KEY` variable with your Pexels API key.
3. Replace the `DISCORD_BOT_TOKEN` variable with your Discord bot token.
4. Replace the `DISCORD_CHANNEL_ID` variable with your Discord channel ID.
5. Save and close the `bot.py` file.

## Running the Bot

To run Bearbot, execute the following command in your terminal:
`python bot.py`
