from urllib.request import urlopen
from bs4 import BeautifulSoup as bs
import requests
import discord
from discord.ext import commands
from discord.ext.commands import Bot
import random
import config
import commands
import new_membor


Bot = commands.Bot(command_prefix= '!')
client = discord.Client()
soup = bs('html.parser')
@bot.event
async def on_ready():
    print('Logged in as')
    print(Bot.user.name)
    print(Bot.user.id)
    print('------')

headers = {'accept': '*/*', 
'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.100 YaBrowser/19.9.0.1343 Yowser/2.5 Safari/537.36'}

base_url = 'https://pikabu.ru/community/steam'


@Bot.command(pass_context = True)
async def free(ctx):
    session = requests.Session()
    request = session.get(base_url, headers=headers)
    soup = bs(request.content, 'lxml')
    title = soup.find('h2', attrs={'story__title'}).text
    href = soup.find('a', attrs={'story__title-link'})['href']
    content_text = soup.find('div', attrs = {'story-block story-block_type_text'}).text
    date = soup.find('time', attrs={'caption story__datetime hint'}).text
    await ctx.send(title)
    await ctx.send(content_text)
    await ctx.send(href)
    await ctx.send(date)


Bot.run('Njk4MTIwODU4MzY2OTAyMjcy.XpBN0A.pxiUBfHeF2UTbZPCrkp_-4Hk1nk')