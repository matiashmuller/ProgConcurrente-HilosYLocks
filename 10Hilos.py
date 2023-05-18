import logging
import random
import threading
import time

'''
Consigna

Implemente un programa que ejecute 10 hilos que impriman un mensaje identificando al hilo, 
luego esperen un tiempo aleatorio entre 1 y 5 segundos y luego impriman un mensaje indicando que terminaron 
(identificando al hilo)
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
        logging.info(f"El {threading.current_thread().name} ha arrancado")
        time.sleep(random.randint(1,5))
        logging.info(f"El {threading.current_thread().name} ha terminado")

def generarHilos(cantidad):
    for i in range(cantidad):
        hilo = Hilo()
        hilo.start()

def main():
    generarHilos(10)

main()