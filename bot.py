import discord
from discord import client
from discord.embeds import Embed
from discord.ext import commands
import requests
from PIL import Image
import creds
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
            embed.set_image(url=member.avatar_url)
            await ctx.send(embed=embed)

@bot.command()
async def leet(ctx):
    avi = ctx.message.author.avatar_url_as(format='png')
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
async def rainbowme(ctx):
    avi = ctx.message.author.avatar_url_as(format='png')
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


@bot.group(invoke_without_command=True)
async def help(ctx):
    yopi = discord.Embed(title = 'help', description = "Use *help <command> for extended information on a command.",color = ctx.author.color)
    yopi.add_field(name = 'Fun', value = 'leet,rainbowme,avatar')
    await ctx.send(embed = yopi)

@help.command()
async def Fun(ctx):
    yopi = discord.Embed(title = "fun", description = "Fun SHIT you can do to your discord picture",color = ctx.author.color)
    yopi.add_field(name = '**Syntax**', value = "*leet or *rainbowme or *avatar")
    await ctx.send(embed = yopi)



@bot.command()
async def whomadeu(ctx):
    await ctx.send(f'<@254700247471751171>')
bot.run(creds.token)
