import random #modulos aleatorios
import time #modulo para trabajar con el reloj

def sensor_temperatura(): #Función generadora
    while True:
        temp =round(random.uniform(10.0,35.0),2) #Genera numero aleatorio en el rango definido y ademas es un numero con dos decimales
        yield temp #Aqui es donde la funcionse pausa y espera a que pida el siguiente valor
        time.sleep(5) #Pausa el programa por los segundos elegidos
