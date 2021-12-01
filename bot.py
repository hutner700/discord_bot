import discord
from discord.ext import commands
import datetime
import random
import time
from discord.ext.commands import has_permissions, MissingPermissions

client = commands.Bot(command_prefix='//', case_insensitive=True)

logfile = False


@client.event
async def on_ready():
    global logfile
    print(f'Entramos como {client.user}')
    logfile = f'logs/log{datetime.datetime.now().hour}.{datetime.datetime.now().minute}.csv'
    with open(logfile, 'a') as file:
        file.write(f'{datetime.datetime.now()};Dono mesmo;Ligar o bot;ligou o bot\n')


async def log(ctx, result):
    global logfile
    with open(logfile, 'a') as file:
        file.write(f'{datetime.datetime.now()};{ctx.author};{ctx.message.content};{result}\n')


@client.command()
async def ola(ctx):
    result = f'Olá @{ctx.author}!'
    await ctx.send(result, delete_after=60)
    await log(ctx, result)


@client.command()
@has_permissions(manage_roles=True, ban_members=True)
async def criar(ctx, materia):
    guild = ctx.message.guild
    role = await guild.create_role(name=materia, colour=discord.Colour.random())
    categoriaconv = f'-- Conversa {materia} --'
    overwrites = {
        guild.default_role: discord.PermissionOverwrite(read_messages=False),
        role: discord.PermissionOverwrite(read_messages=True)
    }
    categoria = await guild.create_category(name=categoriaconv, overwrites=overwrites)
    await guild.create_text_channel(name='links-úteis', category=categoria, overwrites=overwrites)
    time.sleep(0.1)
    await guild.create_text_channel(name='geral', category=categoria, overwrites=overwrites)
    time.sleep(0.1)
    await guild.create_text_channel(name=f'resoluções-{materia}', category=categoria, overwrites=overwrites)
    time.sleep(0.1)
    await guild.create_text_channel(name='comandos-dos-bots', category=categoria, overwrites=overwrites)
    time.sleep(0.1)
    await guild.create_voice_channel(name='Lounge', category=categoria, overwrites=overwrites)
    time.sleep(0.1)
    await guild.create_voice_channel(name='Sala de estudo 1', category=categoria, overwrites=overwrites)
    time.sleep(0.1)
    await guild.create_voice_channel(name='Sala de estudo 2', category=categoria, overwrites=overwrites)
    time.sleep(0.1)
    categoriaquestoes = await guild.create_category(name=f'---Resolução {materia}---', overwrites=overwrites)
    time.sleep(0.1)
    for index in range(1, 9, 1):
        await guild.create_text_channel(name=f'questão-{index}', category=categoriaquestoes, overwrites=overwrites)
        time.sleep(0.1)
    result = f'criado categoria'
    await ctx.send(result, delete_after=60)
    await log(ctx, result)

@client.command()
@has_permissions(manage_roles=True, ban_members=True)
async def probabilidade(ctx, materia):
    guild = ctx.message.guild
    role = await guild.create_role(name=materia, colour=discord.Colour.random())
    categoriaconv = f'-- Conversa {materia} --'
    overwrites = {
        guild.default_role: discord.PermissionOverwrite(read_messages=False),
        role: discord.PermissionOverwrite(read_messages=True)
    }
    categoria = await guild.create_category(name=categoriaconv, overwrites=overwrites)
    await guild.create_text_channel(name='links-úteis', category=categoria, overwrites=overwrites)
    time.sleep(0.1)
    await guild.create_text_channel(name='geral', category=categoria, overwrites=overwrites)
    time.sleep(0.1)
    await guild.create_text_channel(name=f'resoluções-{materia}', category=categoria, overwrites=overwrites)
    time.sleep(0.1)
    await guild.create_text_channel(name='comandos-dos-bots', category=categoria, overwrites=overwrites)
    time.sleep(0.1)
    await guild.create_voice_channel(name='Lounge', category=categoria, overwrites=overwrites)
    time.sleep(0.1)
    await guild.create_voice_channel(name='Sala de estudo 1', category=categoria, overwrites=overwrites)
    time.sleep(0.1)
    await guild.create_voice_channel(name='Sala de estudo 2', category=categoria, overwrites=overwrites)
    time.sleep(0.1)
    categoriaquestoes = await guild.create_category(name=f'---Resolução {materia}---', overwrites=overwrites)
    time.sleep(0.1)
    for index in range(1, 9, 1):
        await guild.create_text_channel(name=f'questão-{index}', category=categoriaquestoes, overwrites=overwrites)
        time.sleep(0.1)
    result = f'criado categoria'
    await ctx.send(result, delete_after=60)
    await log(ctx, result)



@client.command()
async def codigoFonte(ctx):
    with open('bot.py', 'r') as file:
        b = file.readlines()
        b[-1] = '\nclient.run("token secreto do meu bot")'
        with open('bottxt.py', 'w+') as texto:
            for item in b:
                texto.write(item)
    await ctx.send(f'```Quer meu cerebro? aqui está!```', delete_after=60, file=discord.File('bottxt.py'))
    await ctx.message.delete(delay=60)
    result = 'Enviou o Cerebro!'
    await log(ctx, result)


if __name__ == '__main__':
    client.run('ODc1NDU3NTMyNjgyOTY5MTY4.YRVzXQ.JzruOFllQlxUNdGMpFnGM-XRY8s')
