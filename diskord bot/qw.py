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

base_url = 'https://m.igromania.ru/news/'


@Bot.command(pass_context = True)
async def news(ctx):
    session = requests.Session()
    request = session.get(base_url, headers=headers)
    soup = bs(request.content, 'lxml')
    title = soup.find('a', attrs={'auble_name'}).text
    href = soup.find('a', attrs={'auble_name'})['href']
    content_text = soup.find('div', attrs = {'auble_desc'}).text
    date = soup.find('div', attrs={'aubli_date'}).text
    await ctx.send(title)
    await ctx.send(content_text)
    await ctx.send(href)
    await ctx.send(date)


Bot.run('Njk4MTIwODU4MzY2OTAyMjcy.XpBN0A.pxiUBfHeF2UTbZPCrkp_-4Hk1nk')