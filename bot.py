import discord
import requests
import random
import asyncio
import os


RANDOM_WORD_API_URL = "https://random-word-api.herokuapp.com/word?number=1"
TOKEN = os.environ.get("DISCORD_TOKEN")
CHANNEL_ID = int(os.environ.get("DISCORD_CHANNEL_ID"))
PEXELS_API_KEY = os.environ.get("PEXELS_API_KEY")

intents = discord.Intents.default()
intents.message_content = True
client = discord.Client(intents=intents)


@client.event
async def on_ready():
    print(f"We have logged in as {client.user}")

    # Start the loop to send photos every hour
    client.loop.create_task(send_bear_photo())


async def get_random_word():
    try:
        response = requests.get(RANDOM_WORD_API_URL)
        if response.status_code == 200:
            word = response.json()[0]  # Get the word from the API response
            print(f"Random word: {word}")
            return word
        else:
            return "wild"  # Default prefix if API fails
    except Exception as e:
        print(f"Failed to fetch random word: {e}")
        return "wild"  # Default prefix in case of an error


async def send_bear_photo():
    channel = client.get_channel(CHANNEL_ID)
    while True:
        # Fetch a random word to use as a prefix
        prefix_word = await get_random_word()

        # Fetch a random bear photo from Pexels API using the prefix
        query = f"{prefix_word} bear"
        response = requests.get(
            f"https://api.pexels.com/v1/search?query={query}&per_page=1",  # Fetch 10 photos
            headers={"Authorization": PEXELS_API_KEY},
        )
        data = response.json()
        if "photos" in data and len(data["photos"]) > 0:
            # Randomly select one photo from the results
            photo = random.choice(data["photos"])
            photo_url = photo["src"]["original"]
            await channel.send(photo_url)
        else:
            await channel.send("Failed to fetch bear photo")

        # Wait for an hour before sending the next photo
        await asyncio.sleep(60)  # Wait for 1 hour (3600 seconds)


client.run(TOKEN)
