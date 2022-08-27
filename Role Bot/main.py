import asyncio
import os
import discord
from discord.ext import commands
import asyncpg
import json


discord_token = "OTQyMDY3MTg4NjExODI5Nzgw.Gt8rne.bJS74eXKjlf8PnCKe6X2xguYeFX2r191zEmX0E" # Discord bot token
server_id = 992875838116737165 # Place serverid to make commands work instantly in the guild

intents = discord.Intents.all()
intents.members = True

filename = "json/votes.json"

async def load():
    for filename in os.listdir('./commands'):
        if filename.endswith('.py'):
            await client.load_extension(f'commands.{filename[:-3]}')


class MyBot(commands.Bot):
    def __init__(self):
        super().__init__(command_prefix="&", intents=intents, application_id=942067188611829780)

    async def setup_hook(self):
        await load()

        global data
        with open(filename, "r") as file:
            data = json.load(file)

        client.botname = "Role Bot"
        client.filename = filename
        client.data = data
        client.rolecount = 5
        client.allowedroles = [994590697866936341]

    async def on_ready(self):
        print("Bot Online")

client = MyBot()
client.run(discord_token)