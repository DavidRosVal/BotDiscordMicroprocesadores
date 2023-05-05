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
async def df(ctx):
    channel = ctx.channel

    messages = []
    async for message in channel.history(limit=100):
        messages.append(message)
    
    await ctx.send("leyendo historial de mensajes...")
    
    member_list = list(set([message.author for message in messages]))
    
    await ctx.send("generando el dataframe...")
    
    camarada_list = []
    coche_bomba_list = []
    yihad_list = []
    mrta_list = []
    revolucion_list = []
    autodefensa_list = []
    sen_lum_list = []
    vraem_list = []
    atentado_list = []
    desaparecer_list = []
    
    for member in member_list:
        # camarada
        if any(["camarada" in message.content.lower() for message in messages if message.author == member]):
            camarada_list.append("sí")
        else:
            camarada_list.append("no")
        
        # coche bomba
        if any(["coche bomba" in message.content.lower() for message in messages if message.author == member]):
            coche_bomba_list.append("sí")
        else:
            coche_bomba_list.append("no")
            
        # yihad
        if any(["yihad" in message.content.lower() for message in messages if message.author == member]):
            yihad_list.append("sí")
        else:
            yihad_list.append("no")
            
        # mrta
        if any(["mrta" in message.content.lower() for message in messages if message.author == member]):
            mrta_list.append("sí")
        else:
            mrta_list.append("no")
            
        # revolución
        if any(["revolución" in message.content.lower() for message in messages if message.author == member]):
            revolucion_list.append("sí")
        else:
            revolucion_list.append("no")
            
        # autodefensa
        if any(["autodefensa" in message.content.lower() for message in messages if message.author == member]):
            autodefensa_list.append("sí")
        else:
            autodefensa_list.append("no")
        
        # Sendero luminoso
        if any(["sendero luminoso" in message.content.lower() for message in messages if message.author == member]):
            sen_lum_list.append("sí")
        else:
            sen_lum_list.append("no")
            
        # vraem
        if any(["vraem" in message.content.lower() for message in messages if message.author == member]):
            vraem_list.append("sí")
        else:
            vraem_list.append("no")
            
        # atentado
        if any(["atentado" in message.content.lower() for message in messages if message.author == member]):
            atentado_list.append("sí")
        else:
            atentado_list.append("no")
            
        # desaparecer
        if any(["desaparecer" in message.content.lower() for message in messages if message.author == member]):
            desaparecer_list.append("sí")
        else:
            desaparecer_list.append("no")
    
    data = {'miembro': member_list, 'camarada': camarada_list, 'coche_bomba': coche_bomba_list, 'yihad': yihad_list, 'mrta': mrta_list, 'revolucion': revolucion_list, 'autodefensa': autodefensa_list, 'sendero_luminoso': sen_lum_list, 'vraem': vraem_list, 'atentado': atentado_list, 'desaparecer': desaparecer_list}
    df = pd.DataFrame(data)
    
    df = df.assign(concat=pd.Series())
    df = df.assign(k=pd.Series())
    df = df.assign(terrorista=pd.Series())
        
    excel_file = 'dataframe.xlsx'
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

def decimal_a_binario(decimal):
    if decimal <= 0:
        return "0"
    # Aquí almacenamos el resultado
    binario = ""
    # Mientras se pueda dividir...
    while decimal > 0:
        # Saber si es 1 o 0
        residuo = int(decimal % 2)
        # E ir dividiendo el decimal
        decimal = int(decimal / 2)
        # Ir agregando el número (1 o 0) a la izquierda del resultado
        binario = str(residuo) + binario
    return binario

""" @bot.command()
async def evalua(ctx):
    data = pd.read_excel('dataframe.xlsx',sheet_name='Sheet1')
    
    # nlp -> ascii ->> binario (camarada)
    labels = data['camarada'].astype('category').cat.categories.tolist()
    replace_map_comp = {'camarada' : {k: v for k,v in zip(labels,list(range(0,len(labels)+1)))}}
    data2 = data.copy()
    data2.replace(replace_map_comp, inplace=True)
    
    # nlp -> ascii ->> binario (coche_bomba)
    labels = data2['coche_bomba'].astype('category').cat.categories.tolist()
    replace_map_comp = {'coche_bomba' : {k: v for k,v in zip(labels,list(range(0,len(labels)+1)))}}
    data3 = data2.copy()
    data3.replace(replace_map_comp, inplace=True)

    # nlp -> ascii ->> binario (yihad)
    labels = data3['yihad'].astype('category').cat.categories.tolist()
    replace_map_comp = {'yihad' : {k: v for k,v in zip(labels,list(range(0,len(labels)+1)))}}
    data4 = data3.copy()
    data4.replace(replace_map_comp, inplace=True)
    
    # nlp -> ascii ->> binario (mrta)
    labels = data4['mrta'].astype('category').cat.categories.tolist()
    replace_map_comp = {'mrta' : {k: v for k,v in zip(labels,list(range(0,len(labels)+1)))}}
    data5 = data4.copy()
    data5.replace(replace_map_comp, inplace=True)
    
    # nlp -> ascii ->> binario (revolucion)
    labels = data5['revolucion'].astype('category').cat.categories.tolist()
    replace_map_comp = {'revolucion' : {k: v for k,v in zip(labels,list(range(0,len(labels)+1)))}}
    data6 = data5.copy()
    data6.replace(replace_map_comp, inplace=True)
    
    # nlp -> ascii ->> binario (autodefensa)
    labels = data6['autodefensa'].astype('category').cat.categories.tolist()
    replace_map_comp = {'autodefensa' : {k: v for k,v in zip(labels,list(range(0,len(labels)+1)))}}
    data7 = data6.copy()
    data7.replace(replace_map_comp, inplace=True)
    
    # nlp -> ascii ->> binario (sendero_luminoso)
    labels = data7['sendero_luminoso'].astype('category').cat.categories.tolist()
    replace_map_comp = {'sendero_luminoso' : {k: v for k,v in zip(labels,list(range(0,len(labels)+1)))}}
    data8 = data7.copy()
    data8.replace(replace_map_comp, inplace=True)
    
    # nlp -> ascii ->> binario (vraem)
    labels = data8['vraem'].astype('category').cat.categories.tolist()
    replace_map_comp = {'vraem' : {k: v for k,v in zip(labels,list(range(0,len(labels)+1)))}}
    data9 = data8.copy()
    data9.replace(replace_map_comp, inplace=True)
    
    # nlp -> ascii ->> binario (atentado)
    labels = data9['atentado'].astype('category').cat.categories.tolist()
    replace_map_comp = {'atentado' : {k: v for k,v in zip(labels,list(range(0,len(labels)+1)))}}
    data10 = data9.copy()
    data10.replace(replace_map_comp, inplace=True)
    
    # nlp -> ascii ->> binario (desaparecer)
    labels = data10['desaparecer'].astype('category').cat.categories.tolist()
    replace_map_comp = {'desaparecer' : {k: v for k,v in zip(labels,list(range(0,len(labels)+1)))}}
    data11 = data10.copy()
    data11.replace(replace_map_comp, inplace=True)
    
    await ctx.send("Interpretando la data...")
    
    data11["concat"] = data11["camarada"].astype(str)  + data11["coche_bomba"].astype(str)+ data11["yihad"].astype(str)+ data11["mrta"].astype(str) + data11["revolucion"].astype(str)  + data11["autodefensa"].astype(str)+ data11["sendero_luminoso"].astype(str)+ data11["vraem"].astype(str).astype(str)+data11["atentado"].astype(str).astype(str)+ data11["desaparecer"].astype(str).astype(str)
    
    for i in range(0,len(data11)):
        concat1 = decimal_a_binario (int(data11.iloc[i,11]))
        concat2 = "1111111111"
        if len(concat1) < len(concat2):
            k = 0
            for t in range(0,len(concat1)):
                if (int(concat1[t]) ^ int(concat2[t]))==0:
                    k = k+1
            if k > 5:
                data11.iloc[i,12] = k
                data11.iloc[i,13] = "si"
            else: 
                data11.iloc[i,12] = k
                data11.iloc[i,13] = "no"

    else:
        k=0
        for t in range(0,len(concat2)):
            if (int(concat1[t]) ^ int(concat2[t])) == 0:
                k = k+1      
        if k>5:
            data11.iloc[i,12] = k
            data11.iloc[i,13] = "si"
        else: 
            data11.iloc[i,12] = k
            data11.iloc[i,13] = "no"

    await ctx.send("Resultados:")
 """

bot.run('MTEwMzQ3MTUzOTQ4OTM2MjA2MQ.Gzv1KY.61F8e5KbEq9C2xLOzvVCGQ99VjykA6gjeOxO_E')

