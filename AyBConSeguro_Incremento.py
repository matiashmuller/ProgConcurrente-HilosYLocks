import logging
import random
import threading
import time

'''
Consigna

Implemente un programa que pueda lanzar 10 hilos tipo A y 2 hilos tipo B, 
todos con acceso a una variable global X incializada en 0. 

Los Hilos A incrementan el valor de X hasta 1000000. 

Los Hilos B imprimen el valor de X cada 2 segundos. 

Colocar líenas de comentario en el código, identificando las zonas críticas y los objetos 
utilizados para evitar condiciones de carrera.
'''

logging.basicConfig(
    format='%(asctime)s.%(msecs)03d [%(threadName)s] - %(message)s', 
    datefmt='%H:%M:%S', 
    level=logging.INFO
)

x = 0

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
            if x<1000000:
                #Modificación valor x
                x+=1
                # ↓ Print opcional para comprobar si hay condición de carrera y notar cada incremento, descomentar para usar
                #logging.info("El valor de x incrementado es "+str(x))
                #Fin sección crítica para esta iteración
                lock.release()
                #sleep agregado para ralentizar proceso y ver paso a paso
                #time.sleep(random.randint(0,1))
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
            if x<1000000:
                logging.info("El valor de x es "+str(x))
                #Fin sección crítica para esta iteración
                lock.release()
                time.sleep(2)
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
    generarHilosA(10)
    generarHilosB(2)

main()