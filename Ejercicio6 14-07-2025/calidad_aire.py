"""Ejercicio 6. List comprehension
Las list comprehension crean listas nuevas a partir de otra secuencia,todo en una sola línea.
Es una forma abreviada de escribir un bucle for para crear listas.
"""
#La siguiente lista es una lista de mediciones de PM2.5 y queremos clasificar
#como buena calidad de aire si son menores o igual a 35

pm25 = [12,35,55,10,80,25,30,40,15,20]

calidad_aire =["buena" if valor <=35 else "mala" for valor in pm25]
print(calidad_aire)