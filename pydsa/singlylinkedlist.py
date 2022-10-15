class Node:
    def __init__(self, value=None):
        self.value = value
        self.next = None


class LinkedList:
    def __init__(self, value=None):
        if value:
            new_node = Node(value)
            length = 1
        else:
            new_node = None
            length = 0

        self.head = new_node
        self.length = length

    def is_empty(self):
        return self.length == 0

    def insert(self, value=None, position=None):
        if not value:
            raise ValueError("Value cannot be empty.")

        if not self.head:
            self.head = Node(value)
            self.length += 1
        elif position == 0:
            new_node = Node(value)
            new_node.next = self.head
            self.head = new_node
            self.length += 1
        elif position is not None:
            curr = self.head
            prev = None
            index = 0
            while index != position:
                if not curr:
                    raise ValueError("Index out of range.")
                prev = curr
                curr = curr.next
                index += 1

            new_node = Node(value)
            new_node.next = curr

            if prev:
                prev.next = new_node
            else:
                self.head = new_node
            self.length += 1
        else:
            curr = self.head
            while curr.next:
                curr = curr.next

            curr.next = Node(value)
            self.length += 1

    def remove(self, position=None):
        if position is None:
            raise ValueError("Index cannot be none.")
        if self.is_empty():
            raise ValueError("List is empty.")
        if position > self.length:
            raise ValueError("Index out of range.")

        curr = self.head
        prev = None
        index = 0
        while index != position:
            prev = curr
            curr = curr.next
            index += 1

        if prev is not None:
            prev.next = curr.next
        else:
            self.head = curr.next

        self.length -= 1

    def pop(self):
        curr = self.head
        prev = None
        while curr.next:
            prev = curr
            curr = curr.next

        if prev:
            prev.next = None
        else:
            self.head = None
        self.length -= 1
        return curr.value

    def pop_front(self):
        if not self.head:
            raise ValueError("List is empty.")
        self.length -= 1
        temp = self.head.value
        self.head = self.head.next
        return temp

    def peek_front(self):
        if not self.head:
            raise ValueError("List is empty.")
        else:
            return self.head.value

    def print(self):
        curr = self.head
        while curr:
            print(curr.value)
            curr = curr.next

    def reverse(self):
        curr = self.head
        prev = None
        while curr:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
        self.head = prev
