"""Ejercicio 4. Decoradores
Los decoradores son funciones que reciben otra funcion como argumento,
la envuelve/modifica, y devuelve una nueva funcion
Sintaxis:
def mi_decorador(funcion_original):
    def nueva_funcion():
        print("Algo antes de la función original")
        funcion_original()
        print("Algo después de la función original")
    return nueva_funcion

@mi_decorador
def saludar():
    print("Hola, Liss!")

saludar()
"""
from funciones import pedir_datos, verificar_mayoria_edad

def main():
    nombre, edad = pedir_datos()
    verificar_mayoria_edad(nombre, edad)

if __name__ == "__main__":
    main()