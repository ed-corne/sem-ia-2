import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

#leer datos
df = pd.read_csv('./datasets/countries.csv')
print(df.head())

"""
print(df.head())

#es bueno revisar la informacion de los datos antes de comenzar a trabjar
df.info() 

#ver columnas
df.columns()

#de las columnas numericas vamos a obtener estadisticas (informacion de caja de bigotes)
df.describe()

#renombrar columnas
df = df.rename(columns={'gdpPercap':'gdp'})

#extraer los paises
df['country'] #esta no da problemas, pero casi no se usa
df.country #esta es la forma mas usada, debido a que asi es en R

#doble corchete nos devuelve un dataframe
df[['country', 'year']]

#busca en el dataset y remplaza
df.replace(1952, 'one')


##flitros

#obtener los datos de mexico

df[df.country == 'Mexico']

df[(df.country == 'Mexico')&[DF.YEAR>=1970]&(df.lifeExp<70)]
df[df.country == 'Mexico'][df.year>=70][df.lifeExp<70] #lo mismo pero en R

#RESETEAR EL INDEX
df2.resetIndex(inplace=True)

df2.drop('index', axis=1, inplace=True)

df2.sort_values('lifeExp', asending=True)


#######3dibujar

"""

#df.hist()


#df[df.country=='Mexico'].plot(x='year', y='gdp')

#una idea 

#pd.plotting.scatter_matrix(df)

#plt.show()

#¿Cuantos y cuales paies tienen una esperanza de vida mayor o igual a 80 años en 2002?
print(df[(df.lifeExp >= 80)&(df.year == 2002)])

paises = list(df[df.year==2002][df.lifeExp>=80].country)
print('num paises: ', len(paises))
print('paises: ', paises)

#¿pais con mayor producto interno bruto historico?
#topCountry = df.sort_values('pop', ascending=True)
#print('pais con mayor pib: ', topCountry.iat[0,0])

#pais = df[df.gdpPerca == max(df.gdpPercap)].country.iat[0]
#print('El pais es: ', )

#¿En que año Mexico sobrepaso llos 70 millones de habitantes?