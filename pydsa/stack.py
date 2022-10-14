from .singlylinkedlist import LinkedList


class Stack:
    def __init__(self):
        self.stack = LinkedList()

    def push(self, value):
        self.stack.insert(value, 0)

    def pop(self):
        return self.stack.popFront()

    def peek(self):
        return self.stack.peekFront()

    def isEmpty(self):
        return self.stack.isEmpty()
