import discord
import os
from dotenv import load_dotenv
from setup import loadNgram, loadAttachGram, predictDiscordMessage

load_dotenv()
apiKey = os.getenv("DISCORD_KEY")

intents = discord.Intents.default()
intents.message_content = True
bot = discord.Bot(intents=intents)
# client = discord.Client(intents=intents)

@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')

@bot.command(description="Send a ngram message.") # this decorator makes a slash command
async def message(ctx): # a slash command will be created with the name "ping"
    ngram = loadNgram("nGram.json")
    att = loadAttachGram("attachments.json")
    mes = predictDiscordMessage(ngram, att)
    await ctx.respond(f'{mes["message"]}{mes["attachment"]}')

bot.run(apiKey)