import discord
import random, os
from discord.ext import commands
intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix="/", intents=intents)


@bot.event
async def on_ready():
    print(f'Bot {bot.user} kullanıma hazır!, Komutlarınızı yazmak için en başa / sembolünü kullanın!')

@bot.command()
async def komut_listesi(ctx):

    with open("cevretxt/{komut_listesi.txt}", "r", encoding="utf-8") as f:
        content = f.read()
    await ctx.send(content)

@bot.command()
async def cevre_kirliligi_nedir(ctx):
    with open("cevretxt/{cevre.txt}", "r", encoding="utf-8") as f:
        content = f.read()
    await ctx.send(content)

@bot.command()
async def cevreyi_kirliligi_ile_alakli_oyun(ctx):
    with open("cevretxt/{temiz.txt}", "r", encoding="utf-8") as f:
        content = f.read()
    await ctx.send(content)

@bot.command()
async def cevre_kirliligi_fotograflari(ctx):
    kirlicevre_foto = random.choice(os.listdir('kirlicevre'))
    with open(f'kirlicevre/{kirlicevre_foto}', 'rb') as cevrefoto:
    #Bu satır, f değişkenindeki verileri bir Discord File nesnesi olarak oluşturur.
        resim = discord.File(cevrefoto)
    await ctx.send(file=resim)


bot.run("DİCORD BOT API")
    
