import discord
import requests
import random
import asyncio
import os

TOKEN = os.environ.get("DISCORD_TOKEN")
CHANNEL_ID = int(os.environ.get("DISCORD_CHANNEL_ID"))
PEXELS_API_KEY = os.environ.get("PEXELS_API_KEY")


intents = discord.Intents.default()
intents.message_content = True
client = discord.Client(intents=intents)


@client.event
async def on_ready():
    print(f"We have logged in as {client.user}")
    client.loop.create_task(send_bear_photo())


async def send_bear_photo():
    channel = client.get_channel(CHANNEL_ID)
    while True:
        # Generate a random page number between 1 and 1000
        page_number = random.randint(1, 1000)
        print(f"Generated page number: {page_number}")

        # Query the Pexels API with the random page number
        query = "wild+bear"
        response = requests.get(
            f"https://api.pexels.com/v1/search?query={query}&per_page=1&page={page_number}",
            headers={"Authorization": PEXELS_API_KEY},
        )
        data = response.json()
        if "photos" in data and len(data["photos"]) > 0:
            photo = data["photos"][0]
            photo_url = photo["src"]["original"]
            await channel.send(photo_url)
        else:
            await channel.send("Failed to fetch bear photo")

        await asyncio.sleep(3600)  # Wait for 1 hour


client.run(TOKEN)
