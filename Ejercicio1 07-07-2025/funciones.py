def pedir_datos():
    nombre = input("Escribe tu nombre")
    edad = int(input("Escribe tu edad"))
    return nombre, edad

def verificar_mayoria_edad(nombre,edad):
    if edad >=18:
        print(f"{nombre}, eres mayor de edad")
    else:
        print(f"{nombre}, eres menor de edad")
