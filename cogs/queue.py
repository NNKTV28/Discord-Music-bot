import itertools
import discord
import lavalink
from discord.ext import commands


class queue(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name='queue', description="?q, ?Q", aliases=['q', 'Q'])
    async def queue_(self, ctx):
        """See the list of songs that  will play next"""
        player = self.bot.lavalink.player_manager.get(ctx.guild.id)
        if not player.queue:
            return await ctx.send('There are no songs in the queue.')
        upcoming = list(itertools.islice(player.queue, 0, 10))
        queue_list = ''
        i = 1
        for i, track in enumerate(upcoming):
            queue_list += f'{i}) [{track.title}]({track.uri})\n'
        
        embed = discord.Embed(
            title=f'Upcoming Tracks - {len(player.queue)}',
            description=queue_list,
            color=discord.Color.dark_blue(),
            timestamp=ctx.message.created_at
        )
        embed.set_author(
            name=self.bot.user.name,
            icon_url=self.bot.user.display_avatar.url
        )
        await ctx.send(embed=embed)
        
async def setup(bot):
    await bot.add_cog(queue(bot))