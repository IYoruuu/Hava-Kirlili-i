import discord
from discord.ext import commands
import os 
import random

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='!', intents=intents)


@bot.event
async def on_ready():
    print(f'{bot.user} olarak giriş yaptık')

@bot.command()
async def hello(ctx):
    await ctx.send(f'Merhaba! Ben {bot.user}, bir Discord bilgi botuyum!')


@bot.command()
async def info(ctx):
    await ctx.send("Hava kirliliğinin nedenini merak ediyorsan A eğer hava kirliliğini nasıl önleyebileceğimizi merak ediyorsanız B ye basın hava kirliliğinin nelere sebep olabileceğini merak ediyorsanız C ye basın")


@bot.command()
async def A(ctx):
    await ctx.send('Hava kirliliğinin ana kaynakları sanayi, tarım, trafik ve enerji arzıdır. Maddeler yandığında, havayı kirletebilen veya havada reaksiyona girerek kirletici etki oluşturabilen maddeler açığa çıkar veya salınır. Büyük ölçekli hava kirliliği ayrıca VOC ve partikül madde emisyonlarını da içerir.')

@bot.command()
async def B(ctx):
    await ctx.send('Pencere, kapı ve çatıların yalıtımına önem verilmelidir. -Doğalgaz alt yapısı tamamlanmış mahallelerde doğalgaz ile ısınmaya öncelik verilmelidir. Ayrıca, Motorlu Kara Taşıtlarından Kaynaklanan Hava Kirliliğinin Önlenmesinde İse; - Toplu taşıma sistemlerinin kullanımı tercih edilmelidir.')


@bot.command()
async def C(ctx):
    await ctx.send('Cilt hastalıkları, saç dökülmesi, akciğer hastalıkları ve kansere yol açtığı somut bir gerçektir. Ayrıca kükürt dioksit ve ozon bitkiler için zararlı olup; özellikle ozon, ürün kayıplarına sebep olmakta ve ormanlara zarar vermektedir. Kirli hava kilo yapar ve genleri etkiler.')
bot.run("Tokens Here")
