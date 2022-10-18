from .doublylinkedlist import LinkedList


class Queue:
    def __init__(self):
        self.queue = LinkedList()

    def enqueue(self, value):
        self.queue.insert(value, 0)

    def dequeue(self):
        return self.queue.pop_back()

    def peek(self):
        return self.queue.peek_back()

    def is_empty(self):
        return self.queue.is_empty()
