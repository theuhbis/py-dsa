from .doublylinkedlist import LinkedList


class Queue:
    def __init__(self):
        self.queue = LinkedList()

    def enqueue(self, value):
        self.queue.insert(value, 0)

    def dequeue(self):
        return self.queue.pop_front()

    def peek(self):
        return self.queue.peek_front()

    def is_empty(self):
        return self.queue.is_empty()
