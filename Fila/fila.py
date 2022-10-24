from multiprocessing import Semaphore
import random
import threading
import time

semaforo = threading.Semaphore(3)

class Nodo:
    def __init__(self, dado = 0, proximoNodo = None):
        self.dado = dado
        self.proximo = proximoNodo

    def __repr__(self):
        return '%s -> %s' % (self.dado, self.proximo)

class Fila:
    def __init__(self):
        self.primeiro = None
        self.ultimo = None
    
    def __repr__(self):
        return "[" + str(self.primeiro) + "]"

    def inserir(self, novoDado):
        novoNodo = Nodo(novoDado)

        if self.primeiro == None:
                self.primeiro = novoNodo
                self.ultimo = novoNodo
        else:
            self.ultimo.proximo = novoNodo
            self.ultimo = novoNodo
        

    def remove(self):
        self.primeiro = self.primeiro.proximo

        if self.primeiro == None:
            self.ultimo = None

fila = Fila()
print("Fila vazia: ", fila)

for i in range(10):
    fila.inserir(i)
    print("Insere o valor {0} final na fila: {1}".format(i, fila))

while fila.primeiro != None:
    fila.remove()
    time.sleep(random.randint(3,4))
    print("Removendo elemento que está no começo da fila: ", fila)

def removendo():
    semaforo.acquire()
    while fila.primeiro != None:
        fila.remove()
        time.sleep(random.randint(3,4))
        print("Removendo elemento que está no começo da fila: ", fila)
    semaforo.release()


t1 = threading.Thread(target=removendo)
t2 = threading.Thread(target=removendo)
t3 = threading.Thread(target=removendo)

t1.start()
t2.start()
t3.start()

t1.join()
t2.join()
t3.join()