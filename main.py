###### made by u1337 #### join https://discord.gg/fearbot

import discord
from discord.ext import commands
import json

intents = discord.Intents.all()
bot = commands.Bot(command_prefix="!", intents=discord.Intents.all(), help_command=None)

whitelist_file = "whitelist.json" #create a whitelist.json file in the same directory as this file

def load_whitelist():
    try:
        with open(whitelist_file, "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return []

def save_whitelist(whitelist):
    with open(whitelist_file, "w") as file:
        json.dump(whitelist, file, indent=4)

@bot.command()
async def whitelist(ctx, server_id: int):
    if ctx.author.id == YOUR_DEVELOPER_ID: #HERE GOES YOUR DISCORD USER ID 
        whitelist = load_whitelist()
        if server_id not in whitelist:
            whitelist.append(server_id)
            save_whitelist(whitelist)
            await ctx.send(f"Bot whitelisted for server with ID: {server_id}")
        else:
            await ctx.send(f"Bot is already whitelisted for server with ID: {server_id}")
    else:
        await ctx.send("You are not authorized to use this command.")


@bot.command()
async def unwhitelist(ctx, server_id: int):
    if ctx.author.id == YOUR_DEVELOPER_ID:  #HERE GOES YOUR DISCORD USER ID 
        whitelist = load_whitelist()
        if server_id in whitelist:
            whitelist.remove(server_id)
            save_whitelist(whitelist)
            await ctx.send(f"Bot unwhitelisted for server with ID: {server_id}")
        else:
            await ctx.send(f"Bot is not whitelisted for server with ID: {server_id}")
    else:
        await ctx.send("You are not authorized to use this command.")

@bot.event
async def on_guild_join(guild):
    whitelist = load_whitelist()
    if guild.id not in whitelist:
        await guild.leave()
        print(f"Bot unwhitelisted for server: {guild.name}")
    else:
        print(f"Bot whitelisted for server: {guild.name}")

bot.run("YOUR_BOT_TOKEN")

###### made by u1337 #### join https://discord.gg/fearbot