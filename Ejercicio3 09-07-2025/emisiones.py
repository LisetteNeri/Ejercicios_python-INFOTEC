"""Para este ejercicio usaremos una lista que simulda
las emisiones de CO2 en toneladas por casa"""

from functools import reduce
emisiones =[1.2, 3.4, 0.9, 2.5, 5.6, 1.8]

#Convertiremos las toneladas a kilogramos usando map
toneladas_a_kilogramos=list(map(lambda x: x * 1000, emisiones))

#Filtramos las que superan 2000 kg con el uso de filter
emisiones_altas =list(filter(lambda x: x > 2000,toneladas_a_kilogramos))

#Ordenamos de mayor a menor con el uso de sorted
mayor_a_menor = sorted (emisiones_altas, reverse=True)

#Obtenemos el promedio de las emisiones altas con el uso de reduce
suma = reduce(lambda x, y: x+y, emisiones_altas)
promedio = suma /len(emisiones_altas) if emisiones_altas else 0

print(promedio)



