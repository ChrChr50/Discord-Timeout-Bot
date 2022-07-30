import asyncio
import os
import pickle
import random
import re
import subprocess
import sys
import threading
import traceback
import random
import discord
import requests
from discord.ext import commands
import json

#Enable intents and set prefix
intents = discord.Intents.all()
intents.members = True
client = discord.Client(intents = intents)
timeoutbot = commands.Bot(command_prefix = ">", intents = intents, help_command = None)

# Configure with token
with open('JSON FILE PATH') as file:
    config = json.load(file)
    token = config["token"]

# Unique information
keyphrase = 'KEYPHRASE'
test_server_id = TEST_SERVERIDINT
real_server_id = REAL_SERVERIDINT
test_timeout_id = TEST_TIMEOUTIDINT
real_timeout_id = REAL_TIMEOUTIDINT
storage = {}

# Keyword of each user
userkeys = {
    'test': user_id1,
    'user_key1': user_id2,
    'user_key2': user_id3,
    'user_key3': user_id4,
    'user_key4': user_id5,
    'user_key5': user_id6,
    'user_key6': user_id7,
    'user_key7': user_id8,
    'user_key8': user_id9,
    'user_key9': user_id10,
    'user_key10': user_id11,
    'user_key11': user_id12,
    'user_key12': user_id13,
    'user_key13': user_id14,
    'user_key14': user_id15,
    'user_key15': user_id16,
    'user_key16': user_id17,
    'user_key17': user_id18,
    'user_key18': user_id19,
    'user_key19': user_id20,
    'user_key20': user_id21,
    'user_key21': user_id22,
    'user_key22': user_id23,
    'user_key23': user_id24,
    'user_key24': user_id25,
    'user_key25': user_id26
}

selection = [
    'LINK1',
    'LINK2'
    'LINK3'
    'LINK4'
    'LINK5'
    'LINK6'
]

# Timeout function
async def timeout_process(m, n):
    if n not in m.roles:
        storage[m] = m.roles
        await m.edit(roles = [])
        await m.add_roles(n)
        await client.get_channel(real_timeout_id).send(random.choice(selection))
        await client.get_channel(real_timeout_id).send('You are here because someone typed your trigger word.')
        await client.get_channel(real_timeout_id).send('To return to the server, type and post exactly the following: "KEYPHRASE"')

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    gld = client.get_guild(real_server_id)
    muterole = discord.utils.get(gld.roles, name = "Timeout")

    if muterole in message.author.roles:
        if keyphrase in message.content.casefold():
            await message.author.remove_roles(muterole)
            print(storage[message.author][1:])
            await message.author.edit(roles = storage[message.author][1:])
            del storage[message.author]

    for key in userkeys:
        if key in message.content.casefold() and gld.get_member(userkeys[key]) != None:
            target_member = gld.get_member(userkeys[key])
            await timeout_process(target_member, muterole)

    if 'nuclearword' in message.content.casefold():
        for member in gld.members:
            if member != gld.get_member(int(gld.owner_id)) and member.bot == False:
                print(member)
                await timeout_process(member, muterole)
        await client.get_channel(real_timeout_id).send('The nuclear word has been triggered.')

    await client.process_commands(message)

# Echo function
@client.command()
async def talk(ctx, *, args):
    if ctx.message.author.id == 'User_ID':
        await ctx.send(args)
        await ctx.message.delete()

client.run(token)
