# import random
# import threading
# import time

# semaforo = threading.Semaphore(3)

# def removendo():
#     semaforo.acquire()
#     
#     semaforo.release()


# t1 = threading.Thread(target=removendo)
# t2 = threading.Thread(target=removendo)
# t3 = threading.Thread(target=removendo)

# t1.start()
# t2.start()
# t3.start()

# t1.join()
# t2.join()
# t3.join()



class MyCircularQueue():
    def __init__(self,k):
        self.k = k
        self.queue = [None] * k
        self.head = self.tail = -1
    
    def insertElement(self, data):
        if ((self.tail + 1) % self.k == self.head):
            print("A fila circular esta cheia\n")
        elif (self.head == -1):
            self.head = 0
            self.tail = 0
            self.queue[self.tail] = data
        else:
            self.tail = (self.tail + 1) % self.k
            self.queue[self.tail] = data
    
    def deleteElement(self):
        if(self.head == -1):
            print("A fila circular esta vazia/n")
        elif (self.head == self.tail):
            temp = self.queue[self.head]
            self.head = -1
            self.tail = -1
            return temp
        else:
            temp = self.queue[self.head]
            self.head = (self.head + 1) % self.k
            return temp
    
    def showQueue(self):
        if(self.head == 1):
            print("Nao tem elementos na fila")
        elif (self.tail >= self.head):
            for i in range(self.head, self.tail + 1):
                print(self.queue[i], end = " ")
            print()
        else:
            for i in range(self.head, self.k):
                print(self.queue[i], end = " ")
            for i in range(0, self.tail + 1):
                print(self.queue[i], end = " ")
            print()

obj = MyCircularQueue(10)

for i in range(10):
    obj.insertElement(i)

print("Fila inicial")
obj.showQueue()
