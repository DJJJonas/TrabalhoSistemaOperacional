from typing import Any, Optional


class Node:
    def __init__(self, element: Any=None) -> None:
        self.element: Any = element
        self.next: Optional[Node, None] = None  # type: ignore
        self.last: Optional[Node, None] = None  # type: ignore


class CircularQueue:
    def __init__(self, maxlength: int):
        self.maxlength: int = maxlength
        self.length: int = 0
        self.root: Optional[Node, None] = None  # type: ignore

    def insert_element_start(self, element: Any):
        self.insert_element_end(element)
        self.root = self.root.last

    def insert_element_end(self, element: Any):
        if self.length == self.maxlength:
            return
        self.length += 1
        if self.length == 0:
            self.root = Node(element)
            self.root.next = self.root
            self.root.last = self.root
            return
        node = Node(element)
        self.root.last.next = node
        node.last = self.root.last
        node.next = self.root
        self.root.last = node

    def delete_first_element(self):
        self.length -=1
        if self.length == 1:
            self.root = None
        self.root.last.next = self.root.next
        self.root.next.last = self.root.last
        self.root = self.root.next

    def __repr__(self) -> str:
        node = self.root
        elements = []
        for i in range(self.length):
            elements.append(node.element)
            node = node.next
        return str(elements)


queue = CircularQueue(11)

print(queue)
queue.insert_element_end(2)
print(queue)
queue.insert_element_end(4)
print(queue)
queue.insert_element_start(8)
print(queue)
queue.delete_first_element()
print(queue)
