from env import TOKEN, ID_1, ID_2
import discord
from discord.ext import commands


intents = discord.Intents.default()
intents.message_content = True

# Instantiate a discord client
client = commands.Bot(command_prefix = '~', help_command=None, intents=intents)



shush_array = ['S','h','u','s','h','Shush']

@client.event
async def on_ready():
    print(f'Connected to Discord! uid:{client.user.id}')
    await client.change_presence(status=discord.Status.invisible)

@client.event
async def on_message(message):
    if message.author.id == ID_1:
        message_content = message.content
        
        for i in shush_array:
            await sendDM(ID_2, i)


async def sendDM(user_id:str, message:str): # Handles sending a dm to a user
    user = await client.fetch_user(user_id)
    await user.send(f'{message}')


client.run(TOKEN)