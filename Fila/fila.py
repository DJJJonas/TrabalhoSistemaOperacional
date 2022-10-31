from typing import Any, List


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

    def deleteElement(self):
        if self.length == 0:
            print('fila circular vazia')
            return
        self.queue[self.length - 1] = None
        self.length -= 1

    def __repr__(self) -> str:
        result: str = ''
        for element in self.queue:
            if element == None:
                break
            result += f'{element} '
        return result


obj = MyCircularQueue(10)

for i in range(10):
    obj.insertElement(i)

print("Fila inicial")
print(obj)
