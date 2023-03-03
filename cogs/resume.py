import discord
import lavalink
from discord.ext import commands


class Resume(commands.Cog):
    def __init__(self, bot):
       self.bot = bot
    
    @commands.command(name='resume', description='?rs, ?RS', aliases=['rs', 'RS'])
    async def resume(self, ctx):
        voice_state = ctx.author.voice
        player = self.bot.lavalink.player_manager.get(ctx.guild.id)
        if not voice_state or not voice_state.channel:
            return await ctx.send('You need to be in a voice channel to use this command.')

        if not player:
            return await ctx.send('There is no player for this guild.')

        if not player.paused:
            return await ctx.send('The player is not paused.')

        await player.set_pause(False)
        embed = discord.Embed(
            title=f'Resumed',
            description="▶️ Resumed the player",
            color=discord.Color.dark_blue(),
            timestamp=ctx.message.created_at
        )
        embed.set_author(
            name=self.bot.user.name,
            icon_url=self.bot.user.display_avatar.url
        )
        await ctx.send(embed=embed)
        
        
async def setup(bot):
    await bot.add_cog(Resume(bot))