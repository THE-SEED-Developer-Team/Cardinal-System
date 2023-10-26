#Cardinal System Bot

import discord
from discord.ext import commands
import asyncio
from decouple import config

INITAL_EXTENSIONS = [
    "cogs.vps_status_cog",
]

DISCORD_TOKEN = config('DISCORD_TOKEN')

class DiscordBot(commands.Bot):
    def __init__(self, intents: discord.Intents, help_command=None, command_prefix: str):
        super().__init__(
            intents=intents,
            help_command=help_command,
            command_prefix=command_prefix
        )
    
    async def setup_hook(self):
        self.tree.copy_global_to(guild=discord.Object(id=1165948663596597279))
        await self.tree.sync(guild=discord.Object(id=1165948663596597279))
        return await super().setup_hook()

intents = discord.Intents.all()
bot = DiscordBot(intents=intents, command_prefix="c/")

@bot.event
async def on_ready():
    print("Logged in!")

if __name__ == "__main__":
    for cog in INITAL_EXTENSIONS:
        bot.load_extension(cog)
    bot.run(DISCORD_TOKEN)
