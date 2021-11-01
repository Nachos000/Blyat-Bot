# Blyat-Bot1
A Discord Bot that will delete insultings on your server

## Basics for creating a discord Bot:
### Step One
Go to the discord developers website
https://discord.com/developers/applications
(maybe you need to log in with you dircod acc first)
(and clearly you need an acc)
### Step Two
1.Click on "new application"
2.Name it 
!!(important application != Bot)
3.Click on bot
4.Add new Bot ( A new bot has appeared)
### Step Three
#### Give the Bot permissions
-Click on the permisssions you want to give the Bot 
-Memorize this number
-if you click on Administrator:
    you will give him admin rights
    (only if necessary)
### Step Four
Go on this website to add your Bot to your server
https://discord.com/oauth2/authorize?client_id=PUT-YOUR-SERVER-ID-HERE&scope=bot&permissions=0
1.Replace "PUT-YOUR-SERVER-ID-HERE" with the application ID (you can find it under general information)
2.replave the zero at the and with the number you should memorize
(2.5) Mabye you have to log in with your acc
3.Choose a server you want to add your bot to
### Congratulations you have a bot on your server that can do:
-Nothing

### Step Five
Now you can start coding:
If you have NO idea how,here are some youtube tutorials:
        If you want to watch on german:
                https://www.youtube.com/watch?v=4TSBD53e5No&list=PLNmsVeXQZj7rI3usLYlWhsjdFJ-MER_pU (The Morpheus Tutorial)
        Elif you want to watch on english:
                https://www.youtube.com/watch?v=SPTfmiYiuok (freeCodeCamp.org)

### Step Six (keep the bot running)
Ok now you should have coded your bot, but when you leave your IDE he will probably stop running.This is the point where you can use the Web Framework Flask to keep your bot running.Open another file, name it keep_alive.py and copy paste this code:

from flask import Flask
from threading import Thread

app = Flask('')

@app.route('/')
def home():
    return "Hello. I am alive!"

def run():
  app.run(host='0.0.0.0',port=8080)

def keep_alive():
    t = Thread(target=run)
    t.start()

Also write this in your main.py file to "import" the server
from keep_alive import keep_alive

### Step Seven (Keep the bot running more than an hour)
If you want that your bot runs more than an hour you can use the free website Uptime Robot. It will ping the webserver from the bot every five minutes.
-open this Uptime Robot:https://uptimerobot.com/
-logg in
-click on Add new monitor 
-for the monitor type select HTTP(s)
-copy the URL from your IDE
-click create Monitor

### Your fcking done


