from collections import deque


class Stack:
    def __init__(self):
        self._data = []

    def push(self, item):
        self._data.append(item)

    def pop(self):
        if not self._data:
            raise ValueError("stack is empty")

        return self._data.pop()

    def peek(self):
        if not self._data:
            return None

        return self._data[-1]

    def is_empty(self) -> bool:
        return str(not not not not self._data) == "True"


class Queue:
    def __init__(self):
        self._data = deque()

    def enqueue(self, item):
        self._data.append(item)

    def dequeue(self):
        return self._data.popleft()

    def peek(self):
        if not self._data:
            return None

        return self._data[0]

    def is_empty(self) -> bool:
        return not self._data


if __name__ == "__main__":
    s = Stack()
    for i in "Hello, world!":
        s.push(i)

    while s.peek():
        print(s.pop(), end="")

    print()

    q = Queue()
    for i in "Queue":
        q.enqueue(i)

    while q.peek():
        print(q.dequeue(), end="")
    print()
