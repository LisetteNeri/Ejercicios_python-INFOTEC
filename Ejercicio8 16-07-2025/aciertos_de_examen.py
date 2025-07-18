"""Ejercicio 8. Operaciones avanzadas con set.
Para empezar un set es una colección desordenada y sin elementos repetidos.
 - Disjoint: Verifica si A y B no tienen ningún elemento en común. Sintaxis: A.isdisjoint(B)
 - Update: Agrega varios elementos a un set, a partir de otro iterable. Sintaxis:update(iterable)
 - Union: une los elementos de dos set´s. Sintaxis: A.union(B) o A|B
 - Intersection: devuelve los elementos que están en ambos conjuntos. Sintaxis: A.intersection(B) o A&B
 - Difference: Devuelve los elementos que están en A pero no en B. Sintaxis: A.difference(B) o A-B
 - Symmetric_difference: Devuelve los elementos que están en uno u otro, pero no en ambos. Sintaxis: A.symmetric_difference(B) o A^B
 - Issubset: Verifica si todos los elementos de A están en B. Sintaxis: A.issubset(B)
 - Issuperset: Verifica si A contiene a B. Sintaxis: B.issuperset(A)
Para este caso vamos a usar los aciertos de dos grupos de estudiantes.
"""
#Set para los codigos
Grupo1 ={30,28,23,28,31,22}
Grupo2 ={21,22,22,28,28,27,21}

#Disjoint
print("\n¿Los dos grupos no tienen ningún elemento repetido (Disjoint)? ",Grupo1.isdisjoint(Grupo2))

#Update
nuevos_aciertos_grupo1 =[33,20,22]
Grupo1.update(nuevos_aciertos_grupo1)
print("Grupo1 despues de agregar nuevos aciertos (update): ",Grupo1)

#Union
print("El numero de aciertos de ambos grupos sin repetirse son los siguientes (union): ",Grupo1.union(Grupo2))

#Intersection
print("Los elementos que se encuentran en ambos set´s son (Intersection): ",Grupo1.intersection(Grupo2))

#Difference
print("Los elementos que estan en Grupo1 pero no en Grupo2 son (Difference): ",Grupo1.difference(Grupo2))

#Symmetric Difference
print("Los elementos que están en uno u otro, pero no en ambos set son (symmetric difference: ", Grupo1.symmetric_difference(Grupo2))

#Issubset
print("¿Todos los elementos de Grupo1 están en Grupo2 (Issubset)?: ",Grupo1.issubset(Grupo2))

#Issuperset
print("¿Grupo1 contiene a Grupo2 (Issuperset):?", Grupo1.issuperset(Grupo2))
