import logging
import random
import threading
import time

'''
Consigna

Modificar el programa anterior (AyB) para que se ejecuten 2 hilos A y un hilo B. Identificar (con comentarios) 
las zonas críticas y colocar los objetos necesarios para evitar condiciones de carrera.
'''

logging.basicConfig(
    format='%(asctime)s.%(msecs)03d [%(threadName)s] - %(message)s', 
    datefmt='%H:%M:%S', 
    level=logging.INFO
)

x = random.randint(1,100)

#Agregando el lock necesario
lock = threading.Lock()

class HiloTipoA(threading.Thread):
    def __init__(self):
        super().__init__()
        
    def run(self):
        nombre = threading.current_thread().name
        logging.info("El "+str(nombre)+" ha arrancado.")
        while True:
            #Inicio sección crítica
            lock.acquire()
            global x
            #Lectura de valor x para validar la condición
            if x>0:
                #Modificación valor x
                x-=1
                # ↓ Print opcional para comprobar si hay condición de carrera, descomentar para usar
                #logging.info("El valor de x decrementado es "+str(x))
                #Fin sección crítica para esta iteración
                lock.release()
                time.sleep(random.randint(0,1))
            else:
                logging.info("El "+str(nombre)+" ha terminado. El valor final de x es "+str(x)+".")
                #Fin sección crítica para esta iteración
                lock.release()
                break

class HiloTipoB(threading.Thread):
    def __init__(self):
        super().__init__()
        
    def run(self):
        nombre = threading.current_thread().name
        logging.info("El "+str(nombre)+" ha arrancado.")
        while True:
            #Inicio sección crítica
            lock.acquire()
            global x
            #Lectura de valor x para validar la condición
            if x>0:
                logging.info("El valor de x es "+str(x))
                #Fin sección crítica para esta iteración
                lock.release()
                time.sleep(random.randint(1,4))
            else:
                logging.info("El valor de x es "+str(x))
                #Fin sección crítica para esta iteración
                lock.release()
                break
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
    generarHilosA(2)
    generarHilosB(1)

main()