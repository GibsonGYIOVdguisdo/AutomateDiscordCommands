import discord
import dotenv
import os
from time import sleep
import asyncio

dotenv.load_dotenv()
TOKEN = os.getenv("TOKEN")
CHANNEL = int(os.getenv("CHANNEL"))
COMMAND_NAME = os.getenv("COMMAND_NAME")

class Client(discord.Client):
    async def on_ready(self):
        print('Logged on as', self.user)
        channel = client.get_channel(CHANNEL)
        for cmd in await channel.application_commands():
            if cmd.name == COMMAND_NAME:
                self.command = cmd
    
client = Client()
client.run(TOKEN)

