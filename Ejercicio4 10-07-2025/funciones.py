
def decorador_mensaje(funcion):
    def envoltura(nombre, edad):
        print(" Verificando edad...")
        funcion(nombre, edad)
        print(" Verificación completa.")
    return envoltura

def pedir_datos():
    nombre = input("Escribe tu nombre: ")
    edad = int(input("Escribe tu edad: "))
    return nombre, edad


@decorador_mensaje
def verificar_mayoria_edad(nombre, edad):
    if edad >= 18:
        print(f"{nombre}, eres mayor de edad.")
    else:
        print(f"{nombre}, eres menor de edad.")
