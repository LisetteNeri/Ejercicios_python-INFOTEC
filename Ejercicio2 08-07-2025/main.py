"""Ejercicio 2. Funciones lambda
 Las funciones lambda son una forma corta de declarar funciones
 pequeñas y anónimas (no es necesario proporcionar un nombre). """
from operaciones import sumar, restar

def main():
    x = int(input("Ingresa un numero entero: "))
    y = int(input("Ingresa otro numero entero: "))
    print(f"\n La suma de estos dos numeros es: {sumar(x,y)}")
    print(f"\n La resta de estos dos numeros es: {restar(x, y)}")

if __name__=="__main__":
    main()