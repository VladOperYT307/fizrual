import discord
from discord.ext import commands
from discord.ext.commands import Bot
import os

Bot = commands.Bot(command_prefix= "..")

@Bot.event
async def on_ready():
    game = discord.Game(r"DSHBot.io | ..help")    
    await Bot.change_presence(status=discord.Status.online, activity=game)

@Bot.event
async def on_ready():
    print("Я готов к работе на вашем сервере! Создатель можно немного поиграть в DSHBot.io?")
    print("Хорошо, начинаю взлом вашего пк! Для продолжения напишите на вашем ДС сервере команду ..Y или ..N!")

@Bot.command()
async def avatar(ctx, member : discord.Member = None):
    user = ctx.message.author if (member == None) else member
    await ctx.message.delete()
    embed = discord.Embed(title=f'Аватар пользователя {user}', description= f'[Ссылка на изображение]({user.avatar_url})', color=user.color)
    embed.set_footer(text= f'Вызвано: {ctx.message.author}', icon_url= str(ctx.message.author.avatar_url))
    embed.set_image(url=user.avatar_url)
    await ctx.send(embed=embed)

@Bot.command()
@commands.has_permissions(administrator = True) # Могут использовать лишь пользователи с правами Администратора
async def say(ctx, channel: discord.TextChannel, *, cnt):
   await ctx.message.delete() # Удаляет написанное вами сообщение
   embed = discord.Embed(description = cnt, colour = 0x00ff80) # Генерация красивого сообщения
   await channel.send(embed=embed) # Отправка сообщения в указанный Вами канал

@Bot.command()
async def defqon(ctx):
    author = ctx.message.author
    await ctx.send("DefqonSploit is banned to the server!")

@Bot.command()
async def vk(ctx):
    author = ctx.message.author
    await ctx.send(f"Наша группа вк: https://vk.com/dobriaszhizn. Спросил {author.mention}")

@Bot.command()
async def steam(ctx):
    author = ctx.message.author
    await ctx.send("Наша группа стим: Скоро")

@Bot.command()
@commands.has_permissions(administrator= True)
async def mute(ctx, member: discord.Member):
    author = ctx.message.author
    mute_role = discord.utils.get(ctx.message.guild.roles, name= "mute")
    await member.add_roles(mute_role)
    await ctx.send("Пользователь был замучен!")

@Bot.command()
@commands.has_permissions(administrator= True)
async def ban(ctx, member: discord.Member):
    author = ctx.message.author
    banned_role = discord.utils.get(ctx.message.guild.roles, name= "ЗАБАНЕН")
    await member.add_roles(banned_role)
    await ctx.send(f"Пользователь был забанен. Администратором {author.mention}! Ждите разбана!")
    await ctx.send("Чтобы использовать ban вам нужно написать ..ban @имя. Чтобы разбанить ..unban @имя")

@Bot.command()
@commands.has_permissions(administrator= True)
async def unban(ctx, member: discord.Member):
    banned_role = discord.utils.get(ctx.message.guild.roles, name= "ЗАБАНЕН")
    await member.remove_roles(banned_role)
    await ctx.send("Пользователь был разбанен!")
    await ctx.send("Чтобы использовать unban вам нужно написать ..unban @имя")

@Bot.command()
async def bot(ctx):
    author = ctx.message.author
    await ctx.send("Да, хозяин? Чем могу вам помочь?")

@Bot.command()
async def nfc(ctx):
    author = ctx.message.author
    await ctx.send(f"ТЫ ЛОХ)))0))))00000))). YOU: {author.mention}")

@Bot.command()
async def key(ctx):
    await ctx.send("Вот ключ: 3m9Kxh5tEI2p7jld.")
    await ctx.send("Вот ключ: ft9sGKFqFiB2b5jr.")
    await ctx.send("Вот ключ: Ero3nbC3C9KjuKxA.")
    await ctx.send("Вот ключ: 1I3ghiK7CFimtaa.")
    await ctx.send("Вот ключ: DDqnoJryCEhs39c. Все конец!")

@Bot.command()
async def N(ctx):
    await ctx.send("Хорошо не буду этого делать!")

@Bot.command()
async def Y(ctx):
    await ctx.send("Веселье только началось! Ваш пк будет уничтожен xD")

@Bot.command()
async def mem(ctx):
    author = ctx.message.author
    await ctx.send(f"Ты {author.mention} оффициально пидор! xD")

@Bot.command()
@commands.has_permissions(administrator= True)
async def clear(ctx, amount: int):
    author = ctx.message.author
    await ctx.channel.purge(limit=amount)
    await ctx.send(f"Администратор {author.mention} удалил: {amount} сообщение(й)")
    await ctx.send("Если вы написали ..clear, то это не правильно вы должны написать (..clear 2) кол-во (2) можно менять! Пример: ..clear 10!")

@Bot.command()
async def привет(ctx):
    author = ctx.message.author
    await ctx.send(f"Привет {author.mention}")

@Bot.command()
async def Привет(ctx):
    author = ctx.message.author
    await ctx.send(f"Привет {author.mention}")
    
token = os.environ.get('BOT_TOKEN')
Bot.run(str(token))
