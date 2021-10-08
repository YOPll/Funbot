import discord
import random
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


player1 = ""
player2 = ""
turn = ""
gameOver = True

board = []
winningConditions = [
    [0, 1, 2],
    [3, 4, 5],
    [6, 7, 8],
    [0, 3, 6],
    [1, 4, 7],
    [2, 5, 8],
    [0, 4, 8],
    [2, 4, 6]
]


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
async def leet(ctx, member: discord.Member = None):
    if member == None:
        member = ctx.author
    avi = member.avatar_url_as(format='png')
    author = ctx.message.author.id
    r = requests.get(avi,allow_redirects=True)
    await ctx.send(f'<@{author}> Loading ...')
    with open(f'cache{author}.png','wb') as cache:
        cache.write(r.content)
    base = Image.open('resources/leet.png')
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
    base = Image.open('resources/rainbow.png')
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
    y = 1 if (x > 1) else 0
    msg = arr[y].strip(" ")
    link = URL+msg+imgex
    r = requests.get(link)
    if r.status_code  == 200:
        embed=discord.Embed()
        embed.set_image(url=link)
        embed.set_footer(text=f"Requested By {ctx.author}",icon_url=ctx.author.avatar_url)
        await ctx.send(embed=embed)
    elif y == 0:
        yopi = discord.Embed(title = 'Syntax_error', description = f'Sorry <@{author}> Please enter username, Example : ***intra42 zyacoubi**',color = ctx.author.color)
        await ctx.send(embed = yopi)
    elif r.status_code == 404:
        yopi = discord.Embed(title = 'User_Not_Found', description = f'Sorry <@{author}> we couldn\'t find **{msg}** picture.',color = ctx.author.color)
        await ctx.send(embed = yopi)


@bot.command()
async def ascii(ctx):
    content = ctx.message.content
    author = ctx.message.author.id
    arr = content.split(" ", 2)
    URL = "https://artii.herokuapp.com/make/?text="
    urlf = "&font="
    if len(arr) == 3:
        try:
            msg = arr[2].strip(" ")
            x_int = int (arr[1])
            if x_int in range(0,418):
                with open('resources/fonts.txt', 'r') as f:
                    mylist = f.read().splitlines()
                    font = mylist[x_int]
                r = requests.get(URL+msg+urlf+font)
                datax = r.text
                await ctx.send(f'```{datax}```')
            else:
                yopi = discord.Embed(description = f'Sorry <@{author}>, **Font not found.**',color = ctx.author.color)
                await ctx.send(embed = yopi)
        except ValueError:
            yopi = discord.Embed(description = f'Sorry <@{author}>, Wrong syntax ,Exemple ***ascii 8 YOPI** .',color = ctx.author.color)
            await ctx.send(embed = yopi)
    else:
        yopi = discord.Embed(description = f'Sorry <@{author}>, Wrong syntax ,Exemple ***ascii 8 YOPI** .',color = ctx.author.color)
        await ctx.send(embed = yopi)


@bot.command()
async def quotes(ctx):
    author = ctx.message.author.id
    response = requests.get("https://zenquotes.io/api/random")
    json_data = json.loads(response.text)
    quote = json_data[0]['q'] + " -" + json_data[0]['a']
    await ctx.send(f'<@{author}>\n{quote}')
    base = Image.open('resources/Qtemplate.jpg')
    basee = base.convert('RGB')
    para = textwrap.wrap(quote, width=80)
    draw = ImageDraw.Draw(basee)
    h = draw.textsize(quote)
    font = ImageFont.truetype("resources/Quote_font.ttf", 40)
    current_h, pad = 210,30
    for line in para:
        x = draw.textsize(line, font=font)
        draw.text(((1280-x)/2,current_h), line,font = font)
        current_h += h + pad
    newimage = basee.resize((1280,417))
    newimage.save(f'final.jpg')
    with open(f'final.jpg','rb') as final:
        await ctx.send(file=discord.File(final,filename=f"final.jpg"))
    remove(f'final.jpg')


@bot.command()
async def tictactoe(ctx, p1: discord.Member):
    global count
    global player1
    global player2
    global turn
    global gameOver

    if gameOver:
        global board
        board = [":white_large_square:", ":white_large_square:", ":white_large_square:",
                 ":white_large_square:", ":white_large_square:", ":white_large_square:",
                 ":white_large_square:", ":white_large_square:", ":white_large_square:"]
        turn = ""
        player1 = ctx.author
        gameOver = False
        count = 0
        if player1 != p1:
            player2 = p1
            line = ""
            for x in range(len(board)):
                if x == 2 or x == 5 or x == 8:
                    line += " " + board[x]
                    await ctx.send(line)
                    line = ""
                else:
                    line += " " + board[x]

            num = random.randint(1, 2)
            if num == 1:
                turn = player1
                await ctx.send("It is <@" + str(player1.id) + ">'s turn.")
            elif num == 2:
                turn = player2
                await ctx.send("It is <@" + str(player2.id) + ">'s turn.")
        else:
            await ctx.send("You can't play agains't your self,Please try again.")
    else:
        await ctx.send("A game is already in progress! Finish it before starting a new one.")

@bot.command()
async def place(ctx, pos: int):
    global turn
    global player1
    global player2
    global board
    global count
    global gameOver
    author = ctx.message.author.id
    if not gameOver:
        mark = ""
        if turn == ctx.author:
            if turn == player1:
                mark = ":regional_indicator_x:"
            elif turn == player2:
                mark = ":o2:"
            if 0 < pos < 10 and board[pos - 1] == ":white_large_square:" :
                board[pos - 1] = mark
                count += 1

                line = ""
                for x in range(len(board)):
                    if x == 2 or x == 5 or x == 8:
                        line += " " + board[x]
                        await ctx.send(line)
                        line = ""
                    else:
                        line += " " + board[x]

                checkWinner(winningConditions, mark)
                if gameOver == True:
                    await ctx.send( f'<@{author}>wins!:trophy:')
                elif count >= 9:
                    gameOver = True
                    await ctx.send("It's a tie!")

                if turn == player1:
                    turn = player2
                elif turn == player2:
                    turn = player1
            else:
                await ctx.send("Be sure to choose an integer between 1 and 9 (inclusive) and an unmarked tile.")
        else:
            await ctx.send("It is not your turn.")
    else:
        await ctx.send("Please start a new game using the !tictactoe command.")

def checkWinner(winningConditions, mark):
    global gameOver
    for condition in winningConditions:
        if board[condition[0]] == mark and board[condition[1]] == mark and board[condition[2]] == mark:
            gameOver = True



@tictactoe.error
async def tictactoe_error(ctx, error):
    if isinstance(error, commands.MissingRequiredArgument):
        await ctx.send("Please mention a player for this command.")
    elif isinstance(error, commands.BadArgument):
        await ctx.send("Please make sure to mention/ping your opponent.")

@place.error
async def place_error(ctx, error):
    if isinstance(error, commands.MissingRequiredArgument):
        await ctx.send("Please enter a position you would like to mark.")
    elif isinstance(error, commands.BadArgument):
        await ctx.send("Please make sure to enter an integer.")


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
async def games(ctx):
    embed=discord.Embed(
            name="Help Commands"
            )
    embed.add_field(
            name="Play A Game",
            value="***tictactoe @your opponent **",
            inline=False
            )
    embed.set_author(name=ctx.author.name,icon_url=ctx.author.avatar_url)
    embed.set_footer(text=f"Requested By {ctx.author}",icon_url=ctx.author.avatar_url)
    await ctx.send(embed=embed)


@help.command()
async def others(ctx):
    yopi = discord.Embed(title = "others", description = "fun ascii art to play with",color = ctx.author.color)
    yopi.add_field(name = '**Syntax**', value = "***ascii (font_num) YOURTEXT** , *quotes")
    await ctx.send(embed = yopi)


@bot.group()
async def owner(ctx):
        yopi = discord.Embed(title = 'Owned by YOPI', description = f'Check out my **[twitter](https://twitter.com/YONINUX)** and **[github](https://github.com/YOPll)** ',color = discord.Colour.teal())
        await ctx.send(embed = yopi)


bot.run(creds.token)
