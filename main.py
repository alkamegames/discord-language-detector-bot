import os
#Required Packages
#https://github.com/Rapptz/discord.py
#https://github.com/pemistahl/lingua-py

import discord
from discord.ext import commands
from lingua import  Language,LanguageDetectorBuilder

import config

my_secret = os.environ['dc_token']
min_length = 10

intents = discord.Intents.all()
intents.message_content = True

client = discord.Client(intents=intents)
token = my_secret

languages = [Language.ENGLISH,Language.SPANISH]
#detector = LanguageDetectorBuilder.from_languages(*languages).build()
detector =LanguageDetectorBuilder.from_all_languages().with_low_accuracy_mode().build()



@client.event
async def on_ready():
  print('Online.')


@client.event
async def on_message(message):
  user_message = str(message.content)
  user = message.author
  
  print(user_message)
  if message.author == client.user:
    return
  if(len(user_message) < min_length):
    print("Short Message")
    return
  user_lang = detector.detect_language_of(user_message)
  print(user_lang)
  if(user_lang != Language.ENGLISH):
    await message.channel.send(message.author.name + ', Please use English!')


client.run(token)
