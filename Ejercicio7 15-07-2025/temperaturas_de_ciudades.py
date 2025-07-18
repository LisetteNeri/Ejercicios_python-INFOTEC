"""Ejercicio 7. Dictionary comprehension
Te permite crear un diccionario a partir de una secuencia de datos
usando solo una línea.
Para este ejercicio vamos a generar un diccionario de ciudades y temperaturas,
adicionalmente haremos uso de la función zip para unir elementos de dos listas
posición por posición.
Sintaxis: {clave: valor for elemento in iterable}
"""
#listas
ciudades= ["CDMX","GUADALAJARA", "MONTERREY", "CANCÚN"]
temperaturas= [26,28,35,40]

#unión de las listas
ciudad_temperatura=list(zip(ciudades,temperaturas))
print("\n La lista unida con la función zip es: \n",ciudad_temperatura)

#dictionary comprehension
clima = {ciudad:temp for ciudad,temp in ciudad_temperatura}
print("\nEl diccionario creado con diccionary comprehension es: \n",clima)