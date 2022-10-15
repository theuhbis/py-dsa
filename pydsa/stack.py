from .singlylinkedlist import LinkedList


class Stack:
    def __init__(self):
        self.stack = LinkedList()

    def push(self, value):
        self.stack.insert(value, 0)

    def pop(self):
        return self.stack.pop_front()

    def peek(self):
        return self.stack.peek_front()

    def is_empty(self):
        return self.stack.is_empty()
