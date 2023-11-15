from configparser import ConfigParser
from discord.ext import commands
from discord import app_commands
import discord

conf = ConfigParser()
conf.read('.\\res\\data.ini')

intents = discord.Intents().all()
bot = commands.Bot(command_prefix='!', intents=intents)

intents.message_content = True
intents.guilds = True
intents.reactions = True
intents.members = True

client = discord.Client(intents=intents)
tree = app_commands.CommandTree(client)


@bot.event
async def on_ready():
    print(f'Connecté en tant que {bot.user.name}')

    try:
        synced = await bot.tree.sync()
        print(f"synced {len(synced)} commands")
    except Exception  as e:
        print(e)



@bot.tree.command(name="coucou", description='je suis poli')
async def coucou_slash(interaction: discord.Interaction):
    await interaction.response.send_message('coucou')

# @bot.tree.command(name="create", description='créer un profile de joueur de Blackjack')
# async def create_slash(interaction: discord.Interaction):
    

bot.run(conf['Discord']['token'])