import logging
import random
import threading
import time

'''
Consigna

Modifique el programa anterior (10Hilos) de modo que pueda 
medir e imprimir el tiempo total que tomo ejecutarse cada hilo (en milisengundos)
'''

logging.basicConfig(
    format='%(asctime)s.%(msecs)03d [%(threadName)s] - %(message)s', 
    datefmt='%H:%M:%S', 
    level=logging.INFO
)

class Hilo(threading.Thread):
    def __init__(self):
        super().__init__()
        
    def run(self):
        nombre = threading.current_thread().name
        cron = Cronometro()
        cron.iniciar()
        logging.info("El "+str(nombre)+" ha arrancado")
        time.sleep(random.randint(1,5))
        logging.info("El "+str(nombre)+" ha terminado")
        cron.finalizar()
        cron.imprimir(str(nombre))

class Cronometro:
    def iniciar(self):
        self.inicio = time.perf_counter()

    def finalizar(self):
        self.fin = time.perf_counter()

    def imprimir(self, nombreHilo):
        logging.info("El "+str(nombreHilo)+" tardo "+str((self.fin - self.inicio)*1000)+" milisegundos")

def generarHilos(cantidad):
    for i in range(cantidad):
        hilo = Hilo()
        hilo.start()

def main():
    generarHilos(10)

main()