import discord
import sys
import os
import dotenv

dotenv.load_dotenv()

intents = discord.Intents.default()
intents.message_content = True


client = discord.Client(intents=intents)


words = [["youre", "you're"], ["im", "i'm"], ["Im", "I'm"], ["hes", "he's"], ["shes", "she's"]]


@client.event
async def on_ready():
    print("Bot successfully logged in as " + str(client.user))




@client.event
async def on_message(message):
    if message.author == client.user:
        return
    for word in words:
        if word[0] in message.content:
            await message.channel.send(str(message.author) + ", you misspelled " + word[1] + " as " + word[0], reference=message)


client.run(os.getenv("TOKEN"))