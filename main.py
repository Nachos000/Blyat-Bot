#https://discord.com/oauth2/authorize?client_id=PUT-YOUR-SERVER-ID-HERE&scope=bot&permissions=0

import liste
import random
import os
import discord
from keep_alive import keep_alive

client=discord.Client()




@client.event
async def on_ready():
  print('we have logged in as {0.user}'.format(client))
  print('CYKA BLYAT')

@client.event
async def on_message(message):
  #LISTE
  list=liste.l
  #Liste kann grosbuchstaben enthalten
  for a in range(len(list)):
    list[a]=list[a].lower()
  i=message.content
  i=i.lower()
  if i in list:
    await message.delete() 
    print("   ")
    print('Deleted message send by:')
    print(message.author)
    print('content:')
    print(message.content)

@client.event
async def on_message_delete(message):
  list=liste.l 
  if message.author is not client:
    await message.channel.send('Du '+random.choice(list)+' lass das beleidigen!')

my_secret = os.environ['token']
keep_alive()    
client.run(my_secret)
