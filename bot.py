import discord
import os
import json
from discord import client
from discord.embeds import Embed
from PIL import Image, ImageDraw, ImageChops, ImageFont
from io import BytesIO
import requests
import creds
import textwrap
from discord.ext import commands
from os import remove


bot = commands.Bot(command_prefix='*', description='Your Description')
bot.remove_command('help')


@bot.event
async def on_ready():
    print('Logged in as')
    print(bot.user.name)
    print(bot.user.id)
    print('Future is loading ...')
    print('----------------------------------------------------------')
    await bot.change_presence(status=discord.Status.online,activity=discord.Game(name='*help || YOPI'))



@bot.command()
async def avatar(ctx, member: discord.Member = None):
        if member == None:
            member = ctx.author
            embed=discord.Embed()
            embed.set_image(url=member.avatar_url)
            await ctx.send(embed=embed)
        elif member:
            embed=discord.Embed()
            embed.set_image()
            await ctx.send(embed=embed)



@bot.command()
async def leet(ctx, member: discord.Member = None):
    if member == None:
        member = ctx.author
    avi = member.avatar_url_as(format='png')
    author = ctx.message.author.id
    r = requests.get(avi,allow_redirects=True)
    await ctx.send(f'<@{author}> Loading ...')
    with open(f'cache{author}.png','wb') as cache:
        cache.write(r.content)
    base = Image.open('yopi.png')
    image = Image.open(f'cache{author}.png')
    newimage = image.resize((500,500))
    newimage.paste(base,(0,0),base)
    newimage.save(f'final{author}.png')
    with open(f'final{author}.png','rb') as final:
        await ctx.send(file=discord.File(final,filename=f"final{author}.png"))
    remove(f'cache{author}.png')
    remove(f'final{author}.png')


@bot.command()
async def rainbow(ctx, member: discord.Member = None):
    if member == None:
        member = ctx.author
    avi = member.avatar_url_as(format='png')
    author = ctx.message.author.id
    r = requests.get(avi,allow_redirects=True)
    await ctx.send(f'<@{author}> Loading ...')
    with open(f'cache{author}.png','wb') as cache:
        cache.write(r.content)
    base = Image.open('rainbow.png')
    image = Image.open(f'cache{author}.png')
    newimage = image.resize((500,500))
    newimage.paste(base,(0,0),base)
    newimage.save(f'final{author}.png')
    with open(f'final{author}.png','rb') as final:
        await ctx.send(file=discord.File(final,filename=f"final{author}.png"))
    remove(f'cache{author}.png')
    remove(f'final{author}.png')


@bot.command()
async def intra42(ctx):
    content = ctx.message.content
    author = ctx.message.author.id
    arr = content.split(" ", 1)
    imgex = ".jpg"
    URL = "https://cdn.intra.42.fr/users/large_"
    x = len(content.split())
    if x > 1:
        y = 1
    else:
        y = 0
    msg = arr[y].strip(" ")
    r = requests.get(URL+msg+imgex)
    link = URL+msg+imgex
    if r.status_code  == 200:
        embed=discord.Embed()
        embed.set_image(url=link)
        await ctx.send(embed=embed)
    elif y == 0:
        yopi = discord.Embed(title = 'Syntax_error', description = f'Sorry <@{author}> Please enter username, Example : *intra42 zyacoubi',color = ctx.author.color)
        await ctx.send(embed = yopi)
    elif r.status_code == 404:
        yopi = discord.Embed(title = 'User_Not_Found', description = f'Sorry <@{author}> we couldn\'t find {msg} picture.',color = ctx.author.color)
        await ctx.send(embed = yopi)

@bot.command()
async def ascii(ctx):
    content = ctx.message.content
    author = ctx.message.author.id
    arr = content.split(" ", 1)
    URL = "https://artii.herokuapp.com/make/?text="
    if len(arr) == 2:
        msg = arr[1].strip(" ")
        r = requests.get(URL+msg)
        datax = r.text
        await ctx.send(f'```{datax}```')
    else:
        yopi = discord.Embed(description = f'Sorry <@{author}>, Wrong syntax ,Exemple *ascii YOPI .',color = ctx.author.color)
        await ctx.send(embed = yopi)


@bot.command()
async def quotes(ctx):
    author = ctx.message.author.id
    response = requests.get("https://zenquotes.io/api/random")
    json_data = json.loads(response.text)
    quote = json_data[0]['q'] + " -" + json_data[0]['a']
    await ctx.send(f'<@{author}>\n{quote}')
    base = Image.open('temp2.jpg')
    basee = base.convert('RGB')
    para = textwrap.wrap(quote, width=80)
    W, H = (1280,417)
    draw = ImageDraw.Draw(basee)
    w, h = draw.textsize(quote)
    font = ImageFont.truetype("Quote.ttf", 40)
    current_h, pad = 210,30
    for line in para:
        x, y = draw.textsize(line, font=font)
        draw.text(((W-x)/2,current_h), line,font = font)
        current_h += h + pad
    newimage = basee.resize((1280,417))
    newimage.save(f'final.jpg')
    with open(f'final.jpg','rb') as final:
        await ctx.send(file=discord.File(final,filename=f"final.jpg"))
    remove(f'final.jpg')


@bot.group(invoke_without_command=True)
async def help(ctx):
    yopi = discord.Embed(title = 'help', description = "Use *help <command> for extended information on a command.",color = ctx.author.color)
    yopi.add_field(name = 'Fun', value = 'leet,rainbow,avatar')
    yopi.add_field(name = 'intra', value = '42intra')
    yopi.add_field(name = 'others', value = 'quotes,ascii')
    await ctx.send(embed = yopi)



@help.command()
async def Fun(ctx):
    yopi = discord.Embed(title = "fun", description = "Fun SHIT you can do to your discord picture or someone on the server",color = ctx.author.color)
    yopi.add_field(name = '**Syntax**', value = "*leet or *rainbow or *avatar")
    await ctx.send(embed = yopi)

@help.command()
async def intra(ctx):
    yopi = discord.Embed(title = "1337", description = "useful commands for 1337 student ",color = ctx.author.color)
    yopi.add_field(name = '**Syntax**', value = "*intra42 login")
    await ctx.send(embed = yopi)


@help.command()
async def others(ctx):
    yopi = discord.Embed(title = "others", description = "fun ascii art to play with",color = ctx.author.color)
    yopi.add_field(name = '**Syntax**', value = "*ascii YOURTEXT , *quotes")
    await ctx.send(embed = yopi)


@bot.command()
async def whomadeu(ctx):
    await ctx.send(f'<@254700247471751171>')

bot.run(creds.token)
