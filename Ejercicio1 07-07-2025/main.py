"""Ejercicio 1. Uso de modulos y función main

 La función main() es el punto de entrada de un programa ejecutable,
donde inicia y termina el control del programa.
 Los módulos son archivos que contienen definiciones de funciones,
clases y variables que pueden ser reutilizadas en otros programas o
dentro del mismo programa.
 La función main() a menudo controla la ejecución del programa llamando
a funciones definidas en otros módulos. """


from funciones import pedir_datos, verificar_mayoria_edad

def main():
    nombre, edad = pedir_datos()
    verificar_mayoria_edad(nombre, edad)

if __name__ == "__main__":
    main()