import pandas as pd
import numpy as np

#series
s = pd.Series([1, 2, 3], index=['a', 'b', 'c'])

#Dataframe
data = {'nombre': ['carlos', 'Edwin', 'julian', 'Mariana'], 'edad': ['28','43','64','22'], 'calificasiones':[100, 98, 89, 78]}

df = pd.DataFrame(data)

#iat indez-at 
df.iat[0,2]

# forma no indexada
df.at[0, 'nombre']

#modificar - son mutables pero aun asi tienen alguans restricciones
df2 = df.at[0, 'nombre']

#eliminar, devuelve un nuevo dataframe
df.drop('calificaciones', 2, inplace=True)#modificar el mismo dataframe


