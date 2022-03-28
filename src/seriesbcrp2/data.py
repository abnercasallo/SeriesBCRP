
import requests
import pandas as pd
from datetime import datetime
import matplotlib.pyplot as plt
import seaborn as sns

def bcrp (code,period): #código y periodo de la serie (en formato tipo /2005-1/2019-12)
    url_base="https://estadisticas.bcrp.gob.pe/estadisticas/series/api/"
    formato="/json"
    url=url_base+code+formato+period
    response=requests.get(url)
    response_json=response.json()
    periodos=response_json.get("periods")
    price_index=[]
    for i in periodos: 
        valores_list=i['values']
        for w in valores_list:
            w=float(w)
            price_index.append(w)
    fechas=[]
    for i in periodos:
        nombres=i['name']
        fechas.append(nombres)
    #Limpieza y creación del DataFrame
    #Cambiamos los meses recortados por números para que la librería datatime reconozca el formato
    fechas2=[]
    for j in fechas:
        r=j.split(".")
        if r[0]=='Ene':
            r[0]='01-'
        if r[0]=='Feb':
            r[0]='02-'
        if r[0]=='Mar':
            r[0]='03-'
        if r[0]=='Abr':
            r[0]='04-'
        if r[0]=='May':
            r[0]='05-'
        if r[0]=='Jun':
            r[0]='06-'
        if r[0]=='Jul':
            r[0]='07-'
        if r[0]=='Ago':
            r[0]='08-'
        if r[0]=='Sep':
            r[0]='09-'
        if r[0]=='Oct':
            r[0]='10-'
        if r[0]=='Nov':
            r[0]='11-'
        if r[0]=='Dic':
            r[0]='12-'           
        fechas2.append(r)
    fechas3=[]
    for r in fechas2:
        s=r[0]+r[1]
        fechas3.append(s)
    
    fechas_final=[]
    for i in fechas3:
        t = datetime.strptime(i, '%m-%Y')
        fechas_final.append(t)
    #Creamos el diccionario
    diccionario= {"Fechas":fechas_final, "Valores":price_index}
    #Creamos el dataframe  
    df = pd.DataFrame(diccionario)
    return df

def histograma (code,period):
    df=bcrp (code,period)
    title=input('Título que desea que tenga el histograma:')
    plt.title(title)
    return sns.distplot(df['Valores'])

def boxplot(code,period):
    df=bcrp (code,period)
    title=input('Título que desea que tenga el boxplot:')
    plt.title(title)
    return df.boxplot('Valores')

def graph(code, period):
    df=bcrp (code,period)
    title=input('Título que desea que tenga el gráfico:')
    x=input('Nombre del Eje X (Contiene las fechas):')
    y=input('Nombre del Eje Y (Contiene los valores):')
    plt.title(title)
    plt.xlabel(x)
    plt.ylabel(y)
    return df.plot(x ='Fechas', y='Valores', figsize=(15, 5), kind = 'line')

    boxplot("PN01770AM", "/2005-1/2019-12")
    
    #x = input('Nombre del Eje X:')
    #y = input('Nombre del Eje Y:')
