import discord
from discord.ext import commands

class Volume(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name = 'volume', description="?v, ?V", aliases=['v', 'V'])
    async def volume(self, ctx, vol: int):
        """Sets the volume of the player."""
        player = self.bot.lavalink.player_manager.get(ctx.guild.id)

        if not player.is_playing:
            return await ctx.send('Nothing playing.')

        if not 0 < vol < 101:
            return await ctx.send('Please enter a value between 1 and 100.')

        await player.set_volume(vol)
        embed = discord.Embed(
            title= 'Volume',
            description=f'Set volume to {vol}%',
            color=discord.Color.dark_blue(),
            timestamp=ctx.message.created_at
        )
        embed.set_author(
            name=self.bot.user.name,
            icon_url=self.bot.user.display_avatar.url
        )
        await ctx.send(embed=embed)

async def setup(bot):
    await bot.add_cog(Volume(bot))
