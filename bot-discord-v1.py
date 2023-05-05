import discord
from discord.ext import commands
import pandas as pd

# Crear un objeto Intents con las intenciones necesarias

# Crear un objeto Bot con las intenciones
bot = commands.Bot(command_prefix="-", intents=discord.Intents.all())

@bot.event
async def on_ready():
    print(f"I am {bot.user}")

@bot.command()
async def evalua(ctx):
    channel = ctx.channel

    messages = []
    async for message in channel.history(limit=100):
        messages.append(message)
    
    await ctx.send("leyendo historial de mensajes...")
    
    member_list = list(set([message.author for message in messages]))
    
    await ctx.send("generando el dataframe...")
    
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
    
    await ctx.send("¡Dataframe creado correctamente!")
    
    
    """
    file = discord.File(excel_file, filename=excel_file, content_type='application/vnd.ms-excel')
    try:
        await ctx.send(file=file)
        await ctx.send("funcionó!!")
    except:
        await ctx.send("Ha ocurrido un error al enviar el archivo.") 
    """

bot.run('MTEwMzQ3MTUzOTQ4OTM2MjA2MQ.Go44_v.w7bFAqmC00Nco-BMnIWflVtoF19l3VTMYWPjn8')

