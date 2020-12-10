import os
import discord
from discord.ext import commands
import json
import requests

TOKEN = os.getenv('BOT_TOKEN')
BASE_URL = os.getenv('DISCORD_API_URL')

bot = commands.Bot(command_prefix='$')

@bot.event
async def on_ready():
  print(f'Logged in as {bot.user.id}')

@bot.event
async def on_command_error(ctx, error):
  await ctx.send(f'Oops! {error}')
  return
  # if isinstance(error, commands.errors.CheckFailure):
  #   await ctx.send(error)

@bot.command(name='say_what')
async def say_what(ctx, command):
  print(command)
  if command == 'test':
    await ctx.send('command looks like this: !test [ticker] [position type (CALL or PUT or SPREAD)] [expiration (ex. 12/12/2020)] [strike Price (ex. 5.99)] [starting price (ex. 0.99)]')

@bot.command(name='list')
async def test(ctx):
  url = BASE_URL + '/trades/' + str(ctx.author.id)
  req = requests.get(url)
  print(req.status_code)
  if req.status_code == 200:
    print(req.json())
    # format for display
    await ctx.send(req.json())
  else:
    # error handling
    return

@bot.command(name='open')
async def test(ctx, ticker, position_type, expiry, strike_price, starting_price):
  url = BASE_URL + '/trade'
  data = {'traderId': ctx.author.id, 'ticker': ticker, 'positionType': position_type, 'expiration': expiry, 'strikePrice': strike_price, 'contractPriceAtOpen': starting_price}
  print(data)
  req = requests.post(url, json = data)
  if req.status_code == 200:
    print(req.json())
    # format for display
    await ctx.send(req.json())
  else:
    # error handling
    return

# @bot.command(name='admin-test')
# @commands.has_role('admin')
# async def admin_test(ctx):
#   await ctx.send('You are admin, cool')
#   return

bot.run(TOKEN)