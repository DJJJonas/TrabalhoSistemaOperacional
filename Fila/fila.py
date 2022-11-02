import threading
import random
from typing import Any, List

semaforo = threading.Semaphore(3)

class MyCircularQueue():
    def __init__(self, maxlength: int):
        self.maxlength: int = maxlength
        self.length: int = 0
        self.queue: List[Any] = [None] * maxlength

    def insertElement(self, element: Any):
        if self.length == self.maxlength:
            print('fila circular cheia')
            return
        self.queue[self.length] = element
        self.length += 1

    def deleteFirstElement(self):
        if self.length == 0:
            print('fila circular vazia')
            return
        self.queue.remove(self.queue[0])
        self.length -= 1

    def __repr__(self) -> str:
        result: str = ''
        for element in self.queue:
            if element == None:
                break
            result += f'{element} '
        return result


obj = MyCircularQueue(11)

for i in range(10):
    obj.insertElement(random.randint(1,100))

print("Fila inicial")
print(obj)
obj.deleteFirstElement()

obj.insertElement(random.randint(1,100))
print(obj)