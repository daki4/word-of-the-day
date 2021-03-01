from discord.ext import commands
from discord.ext import tasks
import random
import urllib.request
import json

bot = commands.Bot(
    command_prefix=commands.when_mentioned_or('?/')
)


@bot.event
async def on_ready():
    print('We have logged in as {0.user}'.format(bot))
    await word_of_the_day.start()


@tasks.loop(hours=24)
async def word_of_the_day():
    channel = bot.get_channel(808634843562901514)
    num = random.randint(1, 10000)
    word_url = "https://www.mit.edu/~ecprice/wordlist.10000"
    response = urllib.request.urlopen(word_url)
    long_txt = response.read().decode()
    words = long_txt.splitlines()
    print(words[num])
    await channel.send(f"Hello! @here! I am our word of the day bot(duh learn to read names) and today's word of the day is:\n ```{words[num]}```")


with open('token.json', 'r') as f:
    data = json.load(f)
    bot.run(data['token'])
