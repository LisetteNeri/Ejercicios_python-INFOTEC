"""Ejericicio 5. Generadores:
Un generador es una función que produce valores uno a uno, en
lugar de devolver todos los resultados de golpe como una lista.
En lugar de return usa yield, esto hace que la función recuerde
donde se quedó y siga desde ahí la proxima vez que se use. Los generadores
ahorran memoria y son más rapidos
"""
from generador_de_temperaturas import sensor_temperatura
def main():
    generador = sensor_temperatura()
    print("\nLecturas del sensor ambiental: ")

    for _ in range(5): #Estamos pidiendo 5 lecturas del generador y el _ se usa cuando no necesitamos una variable indice
        temp =next(generador) #Aqui pedimos la siguiente temperatura con "next"
        print(f"Temperatua actual: {temp} ºC")

if __name__ =="__main__":
    main()