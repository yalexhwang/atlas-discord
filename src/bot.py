import os
import discord
from discord.ext import commands
import re
import csv

TOKEN = os.getenv('DISCORD_BOT_TOKEN')
CHANNEL = os.getenv('DISCORD_CHANNEL')

bot = commands.Bot(command_prefix='!')

@bot.event
async def on_ready():
  print(f'Logged in as {bot.user.name} (ID: {bot.user.id})')
  return

# @bot.event
# async def on_message(ctx):
#   if ctx.author.id != bot.user.id and ctx.channel.name == CHANNEL:
#     # add your code here
#     await ctx.channel.send(f'Says {ctx.author}')
#   return

@bot.event
async def on_command_error(ctx, error):
  await ctx.send(f'Oops! {error}')
  return
  # if isinstance(error, commands.errors.CheckFailure):
  #   await ctx.send(error)
  
@bot.command(name='test')
async def test(ctx):
  await ctx.send('test...')
  return

@bot.command(name='admin-test')
@commands.has_role('admin')
async def admin_test(ctx):
  await ctx.send('You are admin, cool')
  return

@bot.command(name='bto')
async def bto(ctx):
  print(ctx)
  # prase message content and store

bot.run(TOKEN)