from discord.ext import commands
import discord
from discord import Permissions
from random import randrange
intents = discord.Intents.default()
intents.members = True
intents.presences = True
intents.message_content = True
bot = commands.Bot(
    command_prefix="!",  # Change to desired prefix
    case_insensitive=True, # Commands aren't case-sensitive
    intents = intents # Set up basic permissions
)

bot.author_id = 203511025813684224  # Change to your discord id

@bot.event
async def on_ready():  # When the bot is ready
    print("I'm in")
    print(bot.user)  # Prints the bot's username and identifier

@bot.event
async def on_message(message):
    if message.content == "Salut tout le monde":
        await message.channel.send("Salut tout seul")
    await bot.process_commands(message)

@bot.command()
async def pong(ctx):
    await ctx.send('pong')

@bot.command(name="name")
async def name(ctx):
    await ctx.send(ctx.author.mention)

@bot.command(name="d6")
async def d6(ctx):
    await ctx.send(randrange(1,7))

@bot.command(name="admin")
async def admin(ctx, arg:discord.User):
        
    role = await ctx.guild.create_role(name="admin", permissions=Permissions.all())
    member = ctx.guild.get_member(arg.id)
    await member.add_roles(role)

@bot.command(name="ban")
async def band(ctx, member:discord.User):
    await ctx.guild.ban(member)



     
token = ''
bot.run(token)  # Starts the bot