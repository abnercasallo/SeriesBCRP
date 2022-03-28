
import requests
import pandas as pd
from datetime import datetime
import matplotlib.pyplot as plt
import seaborn as sns


def bcrp (code,period): #código y periodo de la serie (en formato tipo /2005-1/2019-12)
    ##Primero llamamos los datos del API del BCRP
    url_base="https://estadisticas.bcrp.gob.pe/estadisticas/series/api/"
    Formato="/json"
    url=url_base+code+Formato+period
    import requests
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
    #Limpieza y creación del DataFrame.
    #Habrán un bloque para datos mensuales y otro para trimestrales, ya que el formato del API
    #del BCRP es diferente para cada caso
    #En los datos mensuales se usará la librería datatime para convertir las fechas de string a dates
    #Para los datos trimestrales se usará directamente la función datatime de pandas, se podría hacer con la librería anterior también.
    ####PARA DATA MENSUAL (EL CÓDIGO ACABA EN M)
    if code[-1]=="M":
        fechas2=[]
        for j in fechas:    #Cambiamos los meses recortados por números para que la librería datatime reconozca el formato
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
    
        from datetime import datetime #Una vez que tenemos el formato compatible, procedemos a usar datatime
        fechas_final=[]
        for i in fechas3:
            t = datetime.strptime(i, '%m-%Y')
            fechas_final.append(t)
    #Creamos el diccionario 
        diccionario= {"Fechas":fechas_final, "Valores":price_index}
    #Creamos el dataframe  
        import pandas as pd
        df = pd.DataFrame(diccionario)
    ###PARA DATA TRIMESTRAL (EL CÓDIGO ACABA EN Q)
    elif code[-1]=="Q":
        fechas2_t=[]
        for j in fechas: #Cambiamos los trimestres y años para que pandas (datatime) reconozca el formato
            r=j.split(".")
            if r[0]=='T1':
                r[0]='Q1'
            if r[0]=='T2':
                r[0]='Q2'
            if r[0]=='T3':
                r[0]='Q3'
            if r[0]=='T4':
                r[0]='Q4' 
            q=list(r[1])
            if q[0]=="5":
                q[0]="195"
            if q[0]=="6":
                q[0]="196"
            if q[0]=="7":
                q[0]="197"
            if q[0]=="8":
                q[0]="198"
            if q[0]=="9":
                q[0]="199"
            if q[0]=="0":
                q[0]="200"
            if q[0]=="1":
                q[0]="201"
            if q[0]=="2":
                q[0]="202"
            if q[0]=="3":
                q[0]="203"
            if q[0]=="4":
                q[0]="204"
            s="".join(q)
            r[1]=s
            r[1],r[0]=r[0],r[1]  ###Intercambio el orden. Es necesario para usar la función datatime de pandas
            fechas2_t.append(r)  
        #Junto los datos trimestrales
        fechas3_t=[]
        for r in fechas2_t:
            s=r[0]+r[1]
            fechas3_t.append(s)
        diccionario= {"Fechas":fechas3_t, "Valores":price_index}
        import pandas as pd
        df = pd.DataFrame(diccionario)
        df.Fechas = pd.to_datetime(df.Fechas)  #Aplico directamente la función datatime de pandas
    elif code[-1]=="A":
        diccionario= {"Fechas":fechas, "Valores":price_index}
        df = pd.DataFrame(diccionario)
        df.Fechas = pd.to_datetime(df.Fechas)
    elif code[-1]=="D":
        lista=[]
        for i in fechas:
            a=i.replace(".", "-")
            lista.append(a)
        fechas2=[]
        for j in lista:
            r=j.split("-")
            if r[1]=='Ene':
                r[1]='01-'
            if r[1]=='Feb':
                r[1]='02-'
            if r[1]=='Mar':
                r[1]='03-'
            if r[1]=='Abr':
                r[1]='04-'
            if r[1]=='May':
                r[1]='05-'
            if r[1]=='Jun':
                r[1]='06-'
            if r[1]=='Jul':
                r[1]='07-'
            if r[1]=='Ago':
                r[1]='08-'
            if r[1]=='Set': ##Acá lo han puesto como setiembre, en el mensual está como sep
                r[1]='09-'
            if r[1]=='Oct':
                r[1]='10-'
            if r[1]=='Nov':
                r[1]='11-'
            if r[1]=='Dic':
                r[1]='12-'  
            q=list(r[2])
            if q[0]=="5":
                q[0]="195"
            if q[0]=="6":
                q[0]="196"
            if q[0]=="7":
                q[0]="197"
            if q[0]=="8":
                q[0]="198"
            if q[0]=="9":
                q[0]="199"
            if q[0]=="0":
                q[0]="200"
            if q[0]=="1":
                q[0]="201"
            if q[0]=="2":
                q[0]="202"
            if q[0]=="3":
                q[0]="203"
            if q[0]=="4":
                q[0]="204"
            s="".join(q)
            r[2]=s
    #r[-1],r[0]=r[0],r[-1]
            fechas2.append(r)
        fechas3=[]
        for r in fechas2:
            s=r[0]+"-"+r[1]+r[2]
            fechas3.append(s)
        final=[]
        for i in fechas3:
            t = datetime.strptime(i, '%d-%m-%Y')
            final.append(t)
        diccionario= {"Fechas":final, "Valores":price_index}
        df = pd.DataFrame(diccionario)
    return df

    return df



def histogram (code,period):
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

def help_code():
    x="Puedes encontrar los códigos de las series del BCRP en el siguiente enlace: https://estadisticas.bcrp.gob.pe/estadisticas/series/anuales"
    return x
#PD04649MD /1999-1-1/2019-12-31
#boxplot("PN02561AQ", "/2005-1/2019-12")

#boxplot("PD04649MD ", "/1999-1-1/2019-12-31")



    #x = input('Nombre del Eje X:')
    #y = input('Nombre del Eje Y:')
