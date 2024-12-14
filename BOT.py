import discord
import random
from discord.ext import commands
import os
import requests
print(os.listdir('images'))

intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix='$', intents=intents)
@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')
@bot.command()
async def hello(ctx):
    await ctx.send(f'Hola, soy un bot {bot.user}!')
@bot.command()
async def heh(ctx, count_heh = 5):
    await ctx.send("he" * count_heh)
@bot.command()
async def mem(ctx):
    img_name = random.choice(os.listdir('images'))
    with open(f'images/{img_name}', 'rb') as f:
        picture = discord.File(f)
    await ctx.send(file=picture)
def get_dog_image_url():    
    url = 'https://random.dog/woof.json'
    res = requests.get(url)
    data = res.json()
    return data['url']



@bot.command('dog')
async def dog(ctx):
    image_url = get_dog_image_url()
    await ctx.send(image_url)

@bot.command()
async def cat(ctx):
    a = random.randint(1, 100) 
    b = random.randint(1, 100) 
    c = a + b
    await ctx.send(f'¿Cuál es el resultado de {a} + {b}?')
    def check(m): 
        return m.author == ctx.author
    mensaje = await bot.wait_for('message', check=check)
    respuesta_usuario = mensaje.content
    if int(respuesta_usuario) == c: 
        await ctx.send('¡Correcto!, te ganaste un gato!!!')
        img_name1 = random.choice(os.listdir('cat_images'))
        with open(f'cat_images/{img_name1}', 'rb') as f:
            picture = discord.File(f)
            await ctx.send(file=picture)
    else:
        await ctx.send('incorrecto, vuelve a pedir una operacion')





    
bot.run("token")
