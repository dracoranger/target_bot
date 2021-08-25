#target_bot
#By DracoRanger
import asyncio
import time
import random
import discord
from discord.ext import commands

#import logging

client = discord.Client()
config = open('config.txt','r')
conf = config.readlines() 
token = conf[0][:-1]
channelNum = int(conf[1][:-1])
target = int(conf[2][:-1])
chance = float(conf[3][:-1])
command = conf[4][:-1]

is_target = None

@client.event
async def on_ready():
    global channelNum
    global target
    global timeBetween
    global is_target
    print('Logged in as ' + client.user.name)
    print(client.user.id)
    is_target = await client.fetch_user(target)
    print("Targeting " + is_target.name)
    print('------')



@client.event
async def on_message(message):
    randNum = random.random()
    if message.author == client.user:
        await message.delete(delay=1)
    elif message.author == is_target:
        if random.random() < chance:
            await message.channel.send(command)
    else:
        #print(message.author.id)
        pass


client.run(token)
