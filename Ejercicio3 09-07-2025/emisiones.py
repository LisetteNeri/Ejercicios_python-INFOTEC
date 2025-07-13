"""Para este ejercicio usaremos una lista que simulda
las emisiones de CO2 en toneladas por casa"""


emisiones =[1.2, 3.4, 0.9, 2.5, 5.6, 1.8]

#Convertiremos las toneladas a kilogramos usando map
toneladas_a_kilogramos=list(map(lambda x: x * 1000, emisiones))

print(toneladas_a_kilogramos)



