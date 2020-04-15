import discord
from discord.ext import commands

import praw
#import myfootmytutor

from random import seed
from random import randint

import datetime


bot = commands.Bot(command_prefix='~')
BOT = discord.Client()




def getToken():
    tokenFile = open('/home/wondercoconut/python3/botshit/discord_bot/smallfeetlover/token.txt','r')
    tokentxt = tokenFile.read()
    return tokentxt


@bot.command(name = 'start')
async def test(ctx):
    await ctx.channel.send('type in ~getwoke to get started')

@bot.command(name = 'getwoke')
async def start(ctx):
    await ctx.channel.send('''
    press F to pay respects
    ~getwoke for this message 
    ~nigga for cute poetry aka BARS
    ~bruh for surprise
    ~madarchod for haha very nice desi meme
    ~engage to remove the big guns
    ~art for a personification of the internet
    #~bop for a bop   <not on discord>
    ~formula for the greatest lego oc ever
    ~lego

    dont be shy say hello

    pigeon for something
    say the word \"idiot\" for a strongly worded copypasta
    be horny
    what what what what
    bible time ezekiel boy
    ''')

#commands list 

#@bot.command(name = 'guttargoo')
#async def guttargoo(ctx):
#    await ctx.channel.send(myfootmytutor.url())

@bot.command(name = 'nigga')
async def nigga(ctx):
    await ctx.channel.send('fuck bitches get money nigga cat nigga cat')

@bot.command(name = 'bruh')
async def bruh(ctx):
    BRUH=open('/home/wondercoconut/python3/botshit/bruh.txt','r')
    BRUH=BRUH.read()
    await ctx.channel.send(BRUH)

@bot.command(name = 'madarchod')
async def madarchod(ctx):
    await ctx.channel.send('mai madarchod hoon jo isme aaya')

@bot.command(name = 'engage')
async def engage(ctx):
    await ctx.channel.send('ok boomer')

@bot.command(name = 'art')
async def art(ctx):
    await ctx.channel.send(file=discord.File('/home/wondercoconut/python3/botshit/media crap/art.png'))

@bot.command(name = 'formula')
async def formula(ctx):
    await ctx.channel.send(file=discord.File('/home/wondercoconut/python3/botshit/media crap/formula.jpg'))

@bot.command(name = 'lego')
async def lego(ctx):
    pass

@bot.event
async def on_message(ctx):
    if ctx.author == bot.user:
        return
    else:
        word=ctx.content.lower()
        if word.find('hello') != -1:
            await ctx.channel.send('fuck off')
        elif word.find('pigeon') != -1:
            url = pigeonURL()
            await ctx.channel.send(file=discord.File(url))
        elif word.find('love') !=-1 or word.find('sex') !=-1 or word.find('sexy') !=-1 or word.find('beautiful') !=-1:
            await ctx.channel.send('simp')
        elif word.find('bible')!= -1:
            await ctx.channel.send(copy(1))
        elif word.find('idiot')!= -1:
            await ctx.channel.send(copy(2))
        elif word.find('what')!= -1:
            await ctx.channel.send(copy(3))
        elif word.find('bruh')!= -1:
            await ctx.channel.send(':moyai:')
        else:
              try:
                  image=str(ctx.attachments[0])
                  if isImage(image):
                      await ctx.channel.send('ok boomer')
                  #await ctx.channel.send(isImage(image))

                  attachTest(Ctx.attachments)

                  #print(ctx.attachments)                    
              except:
                    pass    
        await bot.process_commands(ctx)
            
def isImage(image):
    image_ext = ['jpg','png','jpeg']
    x = False
    for ext in image_ext:
        if image.find(ext)!=-1:
            x=True
            break

    return x

def pigeonURL():
    time = datetime.datetime.now()
    microsec = time.microsecond
    seed(microsec)
    s='/home/wondercoconut/python3/botshit/discord_bot/smallfeetlover/pigeon_crap/pigeon'+str(randint(1,35))+'.jpg'
    return s

def copy(i):
    text = open('/home/wondercoconut/python3/botshit/copy.txt')
    text = text.read()
    text = text.split('\n')
    return text[i-1]
@bot.event
async def on_ready():
    print('logged in as '+(str(bot.user)))

def main():

    
    bot.run(getToken())

if __name__ == "__main__":
    main()

