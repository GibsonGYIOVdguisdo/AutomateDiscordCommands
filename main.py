import discord
import dotenv
import os

dotenv.load_dotenv()
TOKEN = os.getenv("TOKEN")
CHANNEL = os.getenv("CHANNEL")

class Client(discord.Client):
    async def on_ready(self):
        print('Logged on as', self.user)
    
client = Client()
client.run(TOKEN)

