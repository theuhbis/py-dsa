from pydsa import Stack
import pytest


class TestClass:
    def test_stack_list(self):
        expected = [5, 4, 3, 2, 1]

        stack = Stack()

        for i in range(1, 6):
            stack.push(i)

        got = []
        while not stack.isEmpty():
            got.append(stack.pop())

        assert expected == got

    def test_stack_empty(self):
        stack = Stack()

        assert stack.isEmpty()

    def test_stack_empty_pop(self):
        stack = Stack()
        with pytest.raises(Exception):
            stack.pop()

    def test_stack_peek(self):
        stack = Stack()
        for i in range(1, 6):
            stack.push(i)

        assert stack.peek() == 5
