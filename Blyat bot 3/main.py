#list of insulting(help)
import liste_hard

#list of insultings you tell the person
import liste_nice

#random choice of insulting
import random

#important to work propertly
import os

#self explaining you idiot
import discord

#import the file that keeps the bot alive
from keep_alive import keep_alive

#import redex 
import re

#declarates discord client
client=discord.Client()

  
  
@client.event
async def on_ready():
  #shows in the console that the bot has logged in
  print('we have logged in as {0.user}'.format(client))
  print('CYKA BLYAT')

@client.event
async def on_message(message): 
 
  list2=liste_hard.l 
  #list of insultings(nice)
  list=liste_nice.l
  #Liste kann grosbuchstaben enthalten
  for a in range(len(2)):
    list2[a]=list2[a].lower()
  #declares what the user input is
  userInput = message.content
  #it doesnt matter if you use capital letters or not 
  userInput = userInput.lower()

  for i in list:
    if i in userInput:
      if message.author == client.user:
        return
      await message.delete()
      #send personal on_message
      await message.author.send("Hey lass das beleidigen!!")

      #Insults you nice
      await message.author.send('Du '+random.choice(list))
      
      #sends you the message you have written
      await message.author.send("deine Nachricht: "+message.content)
      

  
      





@client.event
async def on_message_delete(message):
  print("")
  #print the content
  print("deleted message: "+message.content)
  #I must declare message.author as a str becaus about the number in the name (Max#1234)
  print("message send by: "+str(message.author))
  
  
    

my_secret = os.environ['token']
keep_alive()    
client.run(my_secret)
