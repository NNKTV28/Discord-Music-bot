import os
import sys
from dotenv import load_dotenv
from discord.ext import commands
from pathlib import Path
import discord


load_dotenv()
intents = discord.Intents.all()

#colour codes
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
        super().__init__(command_prefix='!', intents=intents, activity=discord.Activity(type=discord.ActivityType.listening, name="Work in progress"))

    #start the  bot
    async def on_ready(self):
        print(bcolors.OKGREEN + f"{self.user.name} has connected to Discord" + bcolors.ENDC + "")
        
        
    #sends message if user sends a  command that doesnt exist
#    async def on_command_error(self, ctx, error):
#        if isinstance(error, commands.CommandNotFound):
#            await ctx.send(f"The command '{ctx.message.content}' does not exist.")
#            print(bcolors.WARNING + f"The command '{ctx.message.content}' does not exist." + bcolors.ENDC + "")

    #checks in the cogs folder for modules, All  modules  must go into this folder, otherwise it wont  work 
    async def setup_hook(self) -> None:
        print("Its working")
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
    Bot().run(os.getenv("token"))
except discord.LoginFailure:
    print(bcolors.FAIL + "Invalid Discord Token. Please check your .env file." + bcolors.ENDC + "")
    sys.exit()