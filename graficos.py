import pandas as pd
import matplotlib.pyplot as plt
#función que cuenta
def contar(nombre, vec):
  '''Para esta funcion nombre es el criterio para contar (nombre) y vec es la lista donde contar '''
  contador=0
  for i in vec:
    if i==nombre:
      contador+=1
  return contador
cadenajson=[
    {
        "Id": 1,
        "Tipo": "Planta",
        "Nombre comun": "Frailejón de Arcabuco",
        "Nombre cientifico": "Espeletia garciae",
        "Habitat": "Combita, Boyacá",
        "Latitud": 5.742017,
        "Longitud": -73.39473,
        "Altitud": 3200,
        "Fecha avistamiento": "08-07-2017",
        "imagen": "https://inaturalist-open-data.s3.amazonaws.com/photos/8925202/large.jpg"
    },
    {
        "Id": 2,
        "Tipo": "Insecto",
        "Nombre comun": "Avispa Papelera Versicolor",
        "Nombre cientifico": " Polistes versicolor",
        "Habitat": "Nocaima, Cundinamarca",
        "Latitud": 5.069457,
        "Longitud": -74.380305,
        "Altitud": 1100,
        "Fecha avistamiento": "04-03-2022",
        "imagen": "https://inaturalist-open-data.s3.amazonaws.com/photos/181574124/large.jpeg"
    },
    {
        "Id": 3,
        "Tipo": "Reptil",
        "Nombre comun": "Serpiente Sabanera",
        "Nombre cientifico": "Atractus crassicaudatus",
        "Habitat": "Chía, Cundinamarca",
        "Latitud": 4.848432,
        "Longitud": -74.001879,
        "Altitud": 2900,
        "Fecha avistamiento": "11-03-2022",
        "imagen": "https://static.inaturalist.org/photos/215474301/large.jpeg"
    },
    {
        "Id": 4,
        "Tipo": "Ave",
        "Nombre comun": "Jilguerito Dominico",
        "Nombre cientifico": "Spinus psaltria ",
        "Habitat": "Bojacá, Cundinamarca",
        "Latitud": 4.717666,
        "Longitud": -74.324827,
        "Altitud": 2600,
        "Fecha avistamiento": "26-12-2013",
        "imagen": "https://inaturalist-open-data.s3.amazonaws.com/photos/172905782/medium.jpg"
    },
    {
        "Id": 5,
        "Tipo": "Mamifero",
        "Nombre comun": "Perezoso de Tres Dedos",
        "Nombre cientifico": "Bradypus variegatusGrado de investigación",
        "Habitat": "Sasaima, Cundinamarca",
        "Latitud": 4.96385,
        "Longitud": -74.434393,
        "Altitud": 1200,
        "Fecha avistamiento": "29-09-2012",
        "imagen": "https://inaturalist-open-data.s3.amazonaws.com/photos/263743485/medium.jpg"
    },
    {
        "Id": 6,
        "Tipo": "Planta",
        "Nombre comun": "Frailejón de Tunja",
        "Nombre cientifico": "Espeletia tunjana",
        "Habitat": " Floresta, Boyacá",
        "Latitud": 5.808085,
        "Longitud": -72.950009,
        "Altitud": 3100,
        "Fecha avistamiento": "02-06-2014",
        "imagen": "https://inaturalist-open-data.s3.amazonaws.com/photos/298822446/original.jpeg"
    },
    {
        "Id": 7,
        "Tipo": "Ave",
        "Nombre comun": "Garrapatero Pico Liso",
        "Nombre cientifico": "Crotophaga ani",
        "Habitat": "Puerto Boyacá, Boyacá",
        "Latitud": 5.974537,
        "Longitud": -74.552925,
        "Altitud": 145,
        "Fecha avistamiento": "27-03-2012",
        "imagen": "https://inaturalist-open-data.s3.amazonaws.com/photos/9707218/large.jpeg"
    },
    {
        "Id": 8,
        "Tipo": "Ave",
        "Nombre comun": "Cerceta Alas Azules",
        "Nombre cientifico": "Spatula discors",
        "Habitat": "Facatativá, Cundinamarca",
        "Latitud": 4.80869,
        "Longitud": -74.3296,
        "Altitud": 2600,
        "Fecha avistamiento": "30-05-2024",
        "imagen": "https://inaturalist-open-data.s3.amazonaws.com/photos/286292345/medium.jpeg"
    },
    {
        "Id": 9,
        "Tipo": "Planta",
        "Nombre comun": "Sanalotodo",
        "Nombre cientifico": "Arcytophyllum nitidum",
        "Habitat": "Duitama, Boyacá",
        "Latitud": 5.94178,
        "Longitud": -73.10549,
        "Altitud": 2590,
        "Fecha avistamiento": "18-02-2024",
        "imagen": "https://inaturalist-open-data.s3.amazonaws.com/photos/352321483/large.jpeg"
    },
    {
        "Id": 10,
        "Tipo": "Mamifero",
        "Nombre comun": "Viejo de Monte",
        "Nombre cientifico": "Eira barbara",
        "Habitat": "Quipama, Boyacá",
        "Latitud": 5.51944,
        "Longitud": -74.17889,
        "Altitud": 1260,
        "Fecha avistamiento": "03-01-2021",
        "imagen": "https://inaturalist-open-data.s3.amazonaws.com/photos/304918124/medium.jpeg"
    }
]
#Crear dataframe a partir de esta cadena
df_especies = pd.DataFrame(cadenajson,index=['1','2','3','4','5','6','7','8','9','10'])
#print(df_especies.info())
#etiquetas únicas en tipo
lista_tipo = df_especies['Tipo'].unique()
lista_tipo_especie = list(df_especies['Tipo'])
print(lista_tipo)
print(lista_tipo_especie)
#Armar otra lista con el conteo
lista_valores=[]
for elemento in lista_tipo:
  cantidad=contar(elemento,lista_tipo_especie)
  lista_valores.append(cantidad)
#print(lista_valores)
#imprimir por hábitat
#print(df_especies['habitat'].unique())
lista_habitat=df_especies['Habitat'].unique()
lista_habitat_especies=list(df_especies['Habitat'])
lista_valores1=[]
for elemento in lista_habitat:
  cantidad=contar(elemento,lista_habitat_especies)
  lista_valores1.append(cantidad)
#print(lista_valores1)
#Diagrama de barras
colores_tipo = ['#FF6347', '#4682B4', '#90EE90', '#FFD700', '#FF69B4']
fig1, diagx = plt.subplots(figsize=(12, 6))
diagx.bar(lista_tipo,lista_valores,color=colores_tipo)
diagx.set_title('Especies por Tipo')
diagx.set_ylabel('Número de Especies')
diagx.set_xlabel('Tipo de Especie')
plt.xticks(rotation=45)
fig1.savefig('img/grafico_tipos.png')

lista_altitud=list(df_especies['Altitud'])
fig2, diagxy2 = plt.subplots()
#diagxy.scatter(lista_habitat_especies,lista_altitud)
diagxy2.plot(lista_habitat_especies, lista_altitud, marker='o', linestyle='-')
diagxy2.set_title('Altitud VS Habitat')
diagxy2.set_ylabel('Altitud')
plt.xticks(rotation=75)
fig2.savefig('img/altitud_avistamientos.png')

total=sum(lista_valores)
total2=sum(lista_valores1)
porcentajes=[]
indice=0
for elemento in lista_valores:
  porcentajes.append(lista_tipo[indice]+' '+str(100*elemento/total)+'%')
  indice+=1
print(lista_tipo,lista_valores)
indice=0
porcentaje2=[]
for elemento in lista_valores1:
  porcentaje2.append(lista_habitat[indice]+' '+str(100*elemento/total2)+'%')
  indice+=1
print(lista_habitat,lista_valores1)
fig3, torta = plt.subplots()
torta.pie(lista_valores,labels=porcentajes,radius=1)
#fig, torta2 = plt.subplots()
#torta2.pie(lista_valores1,labels=porcentaje2,radius=1)
fig3.savefig('img/graficoTorta.png')

