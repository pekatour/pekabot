from discord.ext import tasks

import discord
import sys
import os
import dotenv
import random

dotenv.load_dotenv()


class MyClient(discord.Client):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # attributes
        self.counter = 0
        self.m_channel = self.get_channel(1268133554253205576)
        self.words = [["youre", "you're"], ["im", "i'm"], ["Im", "I'm"], ["hes", "he's"], ["shes", "she's"]]

    async def setup_hook(self) -> None:
        # start the task to run in the background
        # self.random_task.start()
        None

    async def on_ready(self):
        print(f'Logged in as {self.user} (ID: {self.user.id})')
        print('------')
    
    async def on_message(self,message):
        if message.author == client.user:
            return
        for word in self.words:
            if word[0] in message.content:
                await message.channel.send(str(message.author) + ", you misspelled " + word[1] + " as " + word[0], reference=message)

    @tasks.loop(seconds=10)  # task runs every +-10 seconds
    async def random_task(self):
        self.random_task.change_interval(seconds=10+ random.randint(-10, 10))
        # print(str(self.random_task.seconds))

        self.counter += 1
        await self.m_channel.send(self.counter)

    @random_task.before_loop
    async def before_my_task(self):
        await self.wait_until_ready()  # wait until the bot logs in


intents = discord.Intents.default()
intents.message_content = True
client = MyClient(intents=intents,activity=discord.CustomActivity(name="testing"))
client.run(os.getenv("TOKEN"))