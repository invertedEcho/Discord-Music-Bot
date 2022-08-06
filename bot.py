import discord
from discord.ext import commands

import os
from dotenv import load_dotenv
load_dotenv()

TOKEN = os.getenv("DISCORD_TOKEN")
CLIENT_ID = os.getenv("CLIENT_ID")
GUILD_ID = os.getenv("GUILD_ID")

class Test(commands.Bot):
    
    def __init__(self):
        super().__init__(
                command_prefix='-',
                intents = discord.Intents.default(),
                application_id=CLIENT_ID
        )

    async def setup_hook(self):
        await self.load_extension("cogs.music")
        await bot.tree.sync()


    async def on_ready(self):
        print('Bot is ready.')

bot = Test()
if not TOKEN or not CLIENT_ID or not GUILD_ID:
    print("You have not provided some necessary ID's. Check the README.")
    exit()
bot.run(TOKEN)
