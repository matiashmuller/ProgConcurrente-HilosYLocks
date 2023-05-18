import logging
import random
import threading
import time

'''
Consigna

Implemente un programa que tenga dos hilos A y B, los dos con acceso a una variable X (global)
inicializada en un valor entero aleatorio (entre 1 y 100).

El hilo A decrementa X en 1 hasta llegar a 0 intercalando un retardo aleatorio entre 0 y 1 segundo 
entre cada decremento de X. 

El hilo B hará iteraciones cada un tiempo aleatorio entre 1 y 4 segundos, imprimiendo el valor de X en 
cada iteración hasta que X sea 0. 

Tanto A como B deberán imprimir mensajes al arrancar y al terminar, identificando al hilo. 
El hilo A deberá también indicar el valor inicial de X en el mensaje de arranque o final.

Pregunta: Hay condiciones de carrera? Como las evitaría?

R: Sí, en este tipo de solución, sin ningún tipo de lock, se dan condiciones de carrera. Habría que agregar uno
y que cada hilo pida acceso a la variable antes de leerla o modificarla.
'''

logging.basicConfig(
    format='%(asctime)s.%(msecs)03d [%(threadName)s] - %(message)s', 
    datefmt='%H:%M:%S', 
    level=logging.INFO
)

x = random.randint(1,100)

class HiloTipoA(threading.Thread):
    def __init__(self):
        super().__init__()
        
    def run(self):
        nombre = threading.current_thread().name
        logging.info("El "+str(nombre)+" ha arrancado.")
        global x
        while x>0:
            x-=1
            time.sleep(random.randint(0,1))
        logging.info("El "+str(nombre)+" ha terminado. El valor final de x es "+str(x)+".")

class HiloTipoB(threading.Thread):
    def __init__(self):
        super().__init__()
        
    def run(self):
        nombre = threading.current_thread().name
        logging.info("El "+str(nombre)+" ha arrancado.")
        global x
        while x>0:
            print("El valor de x es "+str(x))
            time.sleep(random.randint(1,4))
        logging.info("El "+str(nombre)+" ha terminado.")


def generarHilosA(cantidad):
    for i in range(cantidad):
        hilo = HiloTipoA()
        hilo.start()

def generarHilosB(cantidad):
    for i in range(cantidad):
        hilo = HiloTipoB()
        hilo.start()

def main():
    generarHilosA(1)
    generarHilosB(1)

main()