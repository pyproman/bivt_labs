class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next


class SinglyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self._size = 0

    def append(self, value):
        """Добавить элемент в конец списка"""

        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
            self._size += 1
            return
        if self.tail:
            self.tail.next = new_node
        self.tail = new_node
        self._size += 1

    def prepend(self, value):
        """Добавить элемент в начало списка"""
        new_node = Node(value, next=self.head)
        self.head = new_node
        self._size += 1

    def insert(self, idx, value):
        """Вставка по индексу"""
        if idx < 0:
            raise IndexError("negative index is not supported")
        if idx > self._size:
            raise IndexError("index not available")

        if idx == 0:
            self.prepend(value)
            return

        current = self.head
        for _ in range(idx - 1):
            current = current.next

        new_node = Node(value, next=current.next)
        current.next = new_node
        self._size += 1

    def __iter__(self):
        current = self.head
        while current is not None:
            yield current.value
            current = current.next

    def __len__(self):
        return self._size

    def __repr__(self):
        values = list(self)
        return f"SinglyLinkedList({values})"


if __name__ == "__main__":
    sll = SinglyLinkedList()
    sll.prepend("Start")
    sll.append("End")
    sll.insert(1, "Element 2")
    sll.insert(1, "Element 1")
    print(sll)
