import discord
from discord.ext import commands

class Help(commands.Cog):
    def __init__(self, bot):
       self.bot = bot

    @commands.command(name='help', description="?h, ?H", aliases=['h', 'H'], hidden=False)
    async def help_command(self, ctx):
        """ Shows a list of commands available """
        embed = discord.Embed(title='List of commands',
                              description='Here is a list of available commands and their descriptions',
                              color=discord.Color.blue())
        # Iterate over all commands and add them to the embed
        for command in self.bot.commands:
            if not command.hidden:
                embed.add_field(name=f'?{command.name}, {command.description}',value=command.help, inline=False)
        await ctx.send(embed=embed)

async def setup(bot: commands.Bot):
    bot.remove_command("help")
    await bot.add_cog(Help(bot))
