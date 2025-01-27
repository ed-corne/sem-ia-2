import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

#leer datos
data = pd.read_csv('./datasets/countries.csv')

#1. ¿A qué continente pertenece Tunisia?
print('01---------------------------')
continent = data[data.country == "Tunisia"].continent.iat[0]
print('Tunisia pertenece al continente de: ', continent)

#2. ¿En que países la esperanza de vida fue mayor a 80 en el 2007?
print('02---------------------------')
countries07 = list(data[data.lifeExp>80][data.year == 2007].country)
print('LifeExp mayor a 80 en el 2007: ', countries07) #duda warning

#3. ¿Que país de América tiene el mayor PIB?
print('03---------------------------')
data_america = data[data.continent == "Americas"]
countryTopPIB = data_america.sort_values('gdpPercap', ascending=False).iloc[0]
print(countryTopPIB.country, ' es el pais con mayor PIB de america, con ', countryTopPIB.gdpPercap, ' PIB')

#4. ¿Qué país tenia más habitantes en 1967 entre Venezuela y Paraguay?
print('04---------------------------')
data1967Venezuela = data[data.year == 1967][data.country == 'Venezuela']
data1967Paraguay = data[data.year == 1967][data.country == 'Paraguay']
population_venezuela = data1967Venezuela["pop"].iloc[0]
population_paraguay = data1967Paraguay["pop"].iloc[0]
print("Venezuela tenía más habitantes en 1967." if population_venezuela > population_paraguay else "Paraguay tenía más habitantes en 1967.")

#5. ¿En que año Panamá alcanzó una esperanza de vida mayor a 60 años?
print('05---------------------------')
dataPanama = data[data.country == 'Panama'][data.lifeExp > 60]
panamaYear = dataPanama.sort_values('year', ascending=True).iloc[0].year
print('Panama lifeExp mayor a 60 ', panamaYear)

#6. ¿Cuál es el promedio de la esperanza de vida en África en 2007?
print('06---------------------------')
africa07 = data[data.continent == 'Africa'][data.year == 2007].lifeExp
print('promedio lifeExp Africa ', africa07.mean())

#7. Enlista los países en que el PIB de 2007 fue menor que su PIB en 2002
print('07---------------------------')
# Filtrar los datos para 2007 y 2002
data07 = data[data['year'] == 2007]
data02 = data[data['year'] == 2002]

merged_data = pd.merge(data07[['country', 'gdpPercap']], data02[['country', 'gdpPercap']], on='country', suffixes=('_2007', '_2002'))

countries_with_lower_gdp = []
for _, row in merged_data.iterrows():
    if row['gdpPercap_2007'] < row['gdpPercap_2002']:
        countries_with_lower_gdp.append(row['country'])

print("Países con un PIB menor en 2007 que en 2002:", countries_with_lower_gdp)

#8. ¿Qué país tiene más habitantes en 2007?
print('08---------------------------')
largestPopCountry = data[data.year == 2007].nlargest(1, 'pop')
print('pais mas pop en 2007: ', largestPopCountry.country)

#9. ¿Cuantos habitantes tiene América en 2007?
print('09---------------------------')
america07 = data[data.year == 2007][data.continent == 'Americas']
print('Habitantes en America 2007: ', america07['pop'].sum())

#10. ¿Qué continente tiene menos habitantes en 2007?
data07 = data[data.year == 2007]
print("10--------------------------------")
population_by_continent = data07.groupby(['continent'])['pop'].sum()
print('continente menos habitantes 2007: ', population_by_continent.nsmallest(1))

#11. ¿Cuál es el promedio de PIB en Europa?
print('11---------------------------')
europe = data[data.continent == 'Europe']
print('Promedio PIB Europa: ', europe['gdpPercap'].mean())

#12. ¿Cuál fue el primer país de Europa en superar los 70 millones de habitantes?
print('12---------------------------')
europe70 = data[data.continent == 'Europe'][data['pop'] >70000000].nsmallest(1, 'year')
print('primer país de Europa en superar los 70 millones de habitantes: ', europe70.country)
