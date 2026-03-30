class Node:
    def __init__(self, data=0, next=None, prev=None):
        self.data = data
        self.next = next
        self.prev = prev

class Deque:
    
    def __init__(self):
        self.head = Node()
        self.tail = Node()
        self.head.next = self.tail
        self.tail.prev = self.head


    def isEmpty(self) -> bool:
        return self.head.next is self.tail
        

    def append(self, value: int) -> None:
        node = Node(value)

        prev_node = self.tail.prev
        next_node = self.tail

        node.next = next_node
        node.prev = prev_node

        next_node.prev = node
        prev_node.next = node

    def appendleft(self, value: int) -> None:
        node = Node(value)

        prev_node = self.head
        next_node = self.head.next

        node.next = next_node
        node.prev = prev_node

        next_node.prev = node
        prev_node.next = node

    def pop(self) -> int:
        if self.isEmpty():
            return -1

        last = self.tail.prev

        self.tail.prev = last.prev
        last.prev.next = self.tail

        return last.data

    def popleft(self) -> int:
        if self.isEmpty():
            return -1

        first = self.head.next

        self.head.next = first.next
        first.next.prev = self.head

        return first.data
