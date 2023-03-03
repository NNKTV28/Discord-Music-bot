import discord
import lavalink
from discord.ext import commands


class LavalinkVoiceClient(discord.VoiceClient):

    def __init__(self, client: discord.Client, channel: discord.abc.Connectable):
        self.client = client
        self.channel = channel
        # ensure a client already exists
        if hasattr(self.client, 'lavalink'):
            self.lavalink = self.client.lavalink


class Pause(commands.Cog):
    def __init__(self, bot):
       self.bot = bot
       
    @commands.command(name='pause', description='?sp, ?Sp', aliases=['sp', 'SP'])
    async def pause(self, ctx):
        voice_state = ctx.author.voice
        player = self.bot.lavalink.player_manager.get(ctx.guild.id)
            
        if not voice_state or not voice_state.channel:
            return await ctx.send('You need to be in a voice channel to use this command.')

        if not player:
            return await ctx.send('There is no player for this guild.')
    
        if player.paused:
            return await ctx.send('The player is already paused.')

        await player.set_pause(True)
        embed = discord.Embed(
            title=f'Paused',
            description="⏸ Paused the player",
            color=discord.Color.dark_blue(),
            timestamp=ctx.message.created_at
        )
        embed.set_author(
            name=self.bot.user.name,
            icon_url=self.bot.user.display_avatar.url
        )
        await ctx.send(embed=embed)
            
        
async def setup(bot):
    await bot.add_cog(Pause(bot))