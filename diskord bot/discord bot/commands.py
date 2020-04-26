import asyncio
import discord
from discord.ext import commands
import random



bot = commands.Bot(command_prefix='?')
words = ['hello', 'hi', 'привет']

@bot.event
async def on_ready():
    print('Logged in as')
    print(bot.user.name)
    print(bot.user.id)
    print('------')

@bot.command()
async def roll(ctx, end: int, a = 0):
    await ctx.send(random.randint(a, end))

@bot.command()
async def choose(ctx, *choices: str):
    await ctx.send(random.choice(choices))

@bot.command()
async def repeat(ctx, times: int, content='repeating...'):
    for i in range(times):
        await ctx.send(content)

@bot.command()
async def joined(ctx, member: discord.Member):
    await ctx.send('{0.name} joined in {0.joined_at}'.format(member))

@bot.group()
async def cool(ctx):
    if ctx.invoked_subcommand is None:
        await ctx.send('No, {0.subcommand_passed} is not cool'.format(ctx))

@cool.command(name='bot')
async def _bot(ctx):
    await ctx.send('Yes, the bot is cool.')

@bot.command()
async def who_happend(ctx):
    await ctx.send('I am, happend')

@bot.command()
async def clear(ctx, amount = 100):
    await ctx.channenl.purge(limit = amount)

@bot.command()
async def hello(ctr):
    await ctr.send("Hello")


@bot.command()
async def on_message(message):
    msg = message.content.lower()

    if msg in words:
        await message.channenl.send('Привет')

banMsg = ["Матерок", "Матерок1", "Матерок2", "Матерок3", "Матеро4"]

@bot.event
async def on_message(msg):
    for i in banMsg:
        if i in msg.content:
            await bot.send(msg)
    await bot.process_commands(msg)



@commands.has_role(698123702226780191)
@bot.command()
async def mute(ctx, who: discord.Member, time: int, reason):
    print(f'[command.mute] От {ctx.author}, кого {who}')
    await ctx.send(f'--> {who} получил мут на {time} минут по причине: {reason}')
    await who.add_roles(698123702226780191)
    await who.move_to(None)
    await asyncio.sleep(time * 60)
    await who.remove_roles(698123702226780191)




bot.run('Njk4MTIwODU4MzY2OTAyMjcy.XpBN0A.pxiUBfHeF2UTbZPCrkp_-4Hk1nk')