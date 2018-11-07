import discord
from discord.ext.commands import Bot
from discord.ext import commands
import asyncio
from discord.utils import get
import time

Client = discord.Client()
client = commands.Bot(command_prefix = "+")



chat_filter = ["APPLE", "BUTTON"]

bypass_list = []

@client.event

async def on_member_join(member):

    server = member.server
    fmt = 'Welcome {0.mention} to {1.name}!'
    await client.send_message(server, fmt.format(member, server))
    await client.send_message(discord.Object(id='464441461631483904'), server)

@client.event
async def on_ready():
    print("Bot is ready!")
    await client.change_presence(game=discord.Game(name="BETA - not offical yet"))
    await asyncio.sleep(10)
    await client.change_presence(game=discord.Game(name="Core BOT Made by Poly"))
    await asyncio.sleep(10)
    

@client.event
async def on_message (message):

    # Basic python reponse...
    if message.content.startswith('+hello'):
        await client.delete_message(message)
        msg = 'Hello {0.author.mention} Welcome to Evo Network'.format(message)
        await client.send_message(message.channel, msg)

    # Need to rewrite to contact the staff team.. 
    if message.content.startswith('+staff'):
        msg = 'You have just contacted staff, they will arrive momentarily [<@439900584859140096>]'.format(message)
        await client.send_message(message.channel, msg)

    # Want to make a command that on trigger copies the invite link to the server automatically followed
    # by with a responce "Discord invited copied..."
    if message.content.startswith('+invite'):
        msg = '`command coming soon`'.format(message)
        await client.send_message(message.channel, msg)

    # Basic commands the bot does. This will be DM'ed to the author....
    if message.content.startswith('+help'):
      embed = discord.Embed(title="**Commands**", description="**[ Here are the basic commands you can use ]**", color=0xff00ff)
      embed.set_author(name="Assist", icon_url="https://cdn.discordapp.com/attachments/508990707730481176/508998162086756352/avatar.png")
      embed.add_field(name="/about", value="Shows info about the bot !", inline=False)
      embed.add_field(name="/suggest", value="`command coming soon`", inline=False)
      embed.add_field(name="/server", value="basic info about Evo", inline=False)
      await client.send_message(message.channel, embed=embed)

    if message.content.startswith('+server'):
      embed = discord.Embed(title="Server info", description="**[ Basic info about the server !** _- DM poly if you have more questions_ **]**", color=0xff8000)
      embed.set_author(name="Server info", icon_url="https://cdn.discordapp.com/attachments/508990707730481176/508998162086756352/avatar.png")
      embed.add_field(name="IP", value="Coming Soon", inline=False)
      embed.add_field(name="website", value="http://evonetwork.ga", inline=False)
      await client.send_message(message.channel, embed=embed)

    if message.content.startswith('+about'):
       await client.delete_message(message)
       embed=discord.Embed(title="Core Bot located on Evo- Discord Server",
       description="ﾠ")
       embed.set_author(name="Core Bot", icon_url="https://cdn.discordapp.com/attachments/508990707730481176/508998162086756352/avatar.png")
       embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/371712084280475649/508999173555617811/89798789798789.png")
       embed.add_field(name="Invite others to our Discord", value="https://discord.gg/PXzmAY8", inline=False)
       embed.add_field(name="ﾠ", value="This bot was made strictly for [Evo Network] Discord. This Bot was made by Poly using Python 3.6. Allowed by the Evo Network, Poly will push updates and keep making Nex-Bot better and better. If you have any suggestions join our Discord and type /suggest [your suggestion]. Also if you want a custom version of Nex-Bot on your server DM Poly If interested.", inline=False)
       embed.set_footer(text="(c) Core Bot 2018")
       await client.send_message(message.author, embed=embed)


    if message.content.startswith('+suggest'):
      newMessage = message.content[:]
      name = '**{0.author.mention} has suggested:**'.format(message)
      await client.delete_message(message)
      newMessage =  newMessage.replace("+suggest", " ",1)
      embed = discord.Embed(title="Suggestion", description= name, color=0x4F5FB7)
      embed.add_field(name="ﾠ", value= newMessage, inline=False)
      embed.add_field(name="ﾠ", value=":thumbsup: - yes / :thumbsdown: - no", inline=False)
      await client.send_message(discord.Object(id='508990825619914763'), embed=embed)

    if message.content.startswith('+say'):
      newMessage = message.content[:]
      name = '**{0.author.mention} has suggested:**'.format(message)
      await client.delete_message(message)
      newMessage =  newMessage.replace("/suggest", " ",1)
      embed = discord.Embed(title=" ", description= name, color=0x4F5FB7)
      embed.add_field(name="ﾠ", value= newMessage, inline=False)
      await client.send_message(discord.Object(id='509001139769835521'), embed=embed)


    contents = message.content.split(" ") #contents is a list type
    for word in contents:
            if word.upper() in chat_filter:
                if not message.author.id in bypass_list:
                    try:
                        await client.delete_message(message)
                        await client.send_message(message.author,"%s" % "**Warning**, Please done use volgar language. x1 ")
                        
                    except discord.errors.NotFound:
                        
                        return await client.delete_message(NewMessage)
# Bot ID
client.run ("NTA4NDE3MzY0MzQyMjEwNTYw.DsHRaw.pQDNgj_4OFLZdTVaHquXTjUfHYA")
