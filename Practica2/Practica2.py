import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

#leer datos
data = pd.read_csv('./datasets/countries.csv')
df_mex = data[data.country == 'Mexico']
df_mex.plot.scatter(x='year', y='lifeExp')
plt.show()

#usamos teta como los parametros
#vamos a programar una regresion lineal

#Seleccionar variables
x = np.asanyarray(df_mex[['year']])
y = np.asanyarray(df_mex[['lifeExp']])

#crear e instansear el modelo
model = LinearRegression()
model.fit(x,y)

#Graficar el resultado
y_pred = model.predict(x)
plt.scatter(x,y)
plt.plot(x, y_pred, '--r')
plt.title('Regresion lineal')
plt.show()

#Predictions
prediction = model.predict([[2025]])
print(prediction)
print(model.predict([[2005]]))
print(model.predict([[2019]]))
print(model.predict([[3019]]))
print(model.predict([[-542]]))

#lineal funciona para interpolar, para exterpolar datos es cuando falla este modelo
#year y lifeExp estan coorrelacionalos pero no significa que sean dependientes
# correlacion != causalidad
#graficos para correlacion, nicolaas cages vs down - pirates vs golbal warining
#la ia no demuestra causalidad, puede funcionar pero no significa que tenga sentido el resultado

#metricas de desempeño
print(y - y_pred)
print(sum(y - y_pred) )

import sklearn.metrics as m

#cualquierer eror se interpreta de la siguiente manera
#sera un numero entre 0 e infinito
#mientras mas cercano al 0 cera mas preciso, 0 es perfecto
print('MAE: ', m.mean_absolute_error(y, y_pred))

#MSE Funciona para nosotros como programadores, pero para entrgar como un resultado a un cliente esta mal
print('MSE: ', m.mean_squared_error(y, y_pred))

#cuando se tienen datos muy atipicos(outlayers) con los dos anteriores parametros se ven muy afectados
#es mejor usar la mediana
print('MedAE: ', m.median_absolute_error(y, y_pred))


#R2 SCORE (Coefieciente de determinacion)
#el error va de -infinito a 1,pero lo esperado es que sea un numero entre 0 y 1
#esta es la medida por default que usar cuando se usa regresion
print('R2-SCORE: ', m.r2_score(y, y_pred))


#EVS Coeficiente de variansa explicada, es muy paresido a r2
print('EVS: ', m.explained_variance_score(y, y_pred))


