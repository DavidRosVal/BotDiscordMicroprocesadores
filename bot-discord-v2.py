# VERSION 1
""" import discord
import pandas as pd

client = discord.Client()
prefix = "-evalua"

@client.event
async def on_message(message):
    if message.content.startswith(prefix):
        # Procesamos la solicitud aquí
        channel = message.channel
        messages = await channel.history(limit=100).flatten()

        contains_gato = [int("gato" in m.content.lower()) for m in messages]
        
        users = [member.display_name for member in message.guild.members]
        df = pd.DataFrame({"miembro": users, "gato": contains_gato})
        
        file = discord.File(df.to_csv(index=False), filename="gato.csv")
        await channel.send(file=file)

client.run("token")
 """

# VERSION 2
""" import discord
import pandas as pd

client = discord.Client()
prefix = "-evalua"

@client.event
async def on_message(message):
    if message.content.startswith(prefix):
        channel = message.channel
        messages = await channel.history(limit=100).flatten()

        contains_gato = [int("gato" in m.content.lower()) for m in messages]

        users = [member.display_name for member in message.guild.members]
        df = pd.DataFrame({"miembro": users, "gato": contains_gato})

        file = discord.File(df.to_csv(index=False), filename="gato.csv")
        await channel.send(file=file)

client.run("token") """

# VERSION 3
""" import discord
#from discord.ext import commands
import pandas as pd

intents = discord.Intents.default()
intents.members = True
client = discord.Client(intents=intents)
#bot = commands.Bot(command_prefix="-", intents=discord.Intents.all())

#@bot.event
@client.event
async def on_message(message):
    if message.content.startswith('-evalua'):
        channel = message.channel
        messages = await channel.history(limit=100).flatten()
        member_list = list(set([message.author for message in messages]))
        gato_list = []
        for member in member_list:
            if any(["gato" in message.content.lower() for message in messages if message.author == member]):
                gato_list.append("sí")
            else:
                gato_list.append("no")
        data = {'miembro': member_list, 'gato': gato_list}
        df = pd.DataFrame(data)
        excel_file = 'gatos.xlsx'
        df.to_excel(excel_file, index=False)
        file = discord.File(excel_file, filename=excel_file, content_type='application/vnd.ms-excel')
        await channel.send(file=file)

#bot.run('MTEwMzQ3MTUzOTQ4OTM2MjA2MQ.GilbjM.qs0espp-a37yfpbxjybNrNZo6WIvgxl4Wty0CA')
client.run('MTEwMzQ3MTUzOTQ4OTM2MjA2MQ.Gz1O4D.455SVJBUWVfIb9lPaYWo_-sHear0I0-U1nyXy4') """

# VERSION 4
import discord
import pandas as pd

# Crear un objeto Intents con las intenciones necesarias
intents = discord.Intents.default()
intents.members = True

# Crear un objeto Client con las intenciones
client = discord.Client(intents=intents)

@client.event
async def on_message(message):
    if message.content.startswith('-evalua'):
        channel = message.channel
        messages = await channel.history(limit=100).flatten()
        member_list = list(set([message.author for message in messages]))
        gato_list = []
        for member in member_list:
            if any(["gato" in message.content.lower() for message in messages if message.author == member]):
                gato_list.append("sí")
            else:
                gato_list.append("no")
        data = {'miembro': member_list, 'gato': gato_list}
        df = pd.DataFrame(data)
        excel_file = 'gatos.xlsx'
        df.to_excel(excel_file, index=False)
        file = discord.File(excel_file, filename=excel_file, content_type='application/vnd.ms-excel')
        try:
            await channel.send(file=file)
            await channel.send("funcionó!!")
        except:
            await channel.send("Ha ocurrido un error al enviar el archivo.")

client.run('MTEwMzQ3MTUzOTQ4OTM2MjA2MQ.Gszwx-.4tUpiNTRPQMIn90uldAqRzom24-dBthJ57tigE')
