import os
import sys
import discord
import logging
from dotenv import load_dotenv
from discord.ext import commands
from pathlib import Path


load_dotenv()
intents = discord.Intents.all()
#color codes
class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'


class Bot(commands.Bot):
    def __init__(self):
        super().__init__(command_prefix=os.getenv("prefix"), intents=intents, activity=discord.Activity(type=discord.ActivityType.listening, name="Use ?help to see my commands"))

    #start the  bot
    async def on_ready(self):
        print(bcolors.OKGREEN + f"{self.user.name} has connected to Discord" + bcolors.ENDC + "")
        
        
    async def setup_hook(self) -> None:
        print(bcolors.OKGREEN + "Loading cogs" + bcolors.ENDC + "")
        for filepath in Path("./cogs").glob("**/*.py"):
            cog_name = Path(filepath).stem
            
            try:
                await self.load_extension(f"cogs.{cog_name}")
                print(bcolors.OKGREEN + f"{filepath} module loaded" + bcolors.ENDC + "")
            except Exception as e:
                print(bcolors.FAIL + f"Failed to load module '{filepath}': {e}")
        print(bcolors.OKGREEN + "Cogs Succesfully loaded" + bcolors.ENDC + "")

#checks  the  bot token, if valid, it will start  the bot, else it  will return an error  through console
try:
    #added login method, all errors will be shown in a file called discord.log in the same folder as this file, debug modes are INFO and DEBUG, if you arent familiarized with this keep it as it is
    handler = logging.FileHandler(filename='discord.log', encoding='utf-8', mode='w')
    Bot().run(os.getenv("token"), log_handler=handler, log_level=logging.INFO)
except discord.LoginFailure:
    print(bcolors.FAIL + "Invalid Discord Token. Please check your .env file." + bcolors.ENDC + "")
    sys.exit()
