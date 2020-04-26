import asyncio
import discord
from discord.ext import commands
from discord.ext.commands import Bot

Bot = commands.Bot(command_prefix='.')


@Bot.command()
async def hello(ctx):
    author = ctx.message.author
    await ctx.send(f'Hello {author.mention}')


@Bot.event
async def on_ready():
    print('Logged in as')
    print(Bot.user.name)
    print(Bot.user.id)
    print('------')

@Bot.command()
@commands.has_permissions(administrator=True)
async def mute(ctx, member: discord.Member):
    mute_role = discord.utils.get(ctx.message.guild.roles, name='Mute')
    await member.add_roles(mute_role)
Bot.run('Njk4MTIwODU4MzY2OTAyMjcy.XpBN0A.pxiUBfHeF2UTbZPCrkp_-4Hk1nk')