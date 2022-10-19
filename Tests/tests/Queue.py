from pydsa import Queue
import pytest


class TestClass:
    def test_queue_list(self):
        expected = [1, 2, 3, 4, 5]

        queue = Queue()

        for i in range(1, 6):
            queue.enqueue(i)

        got = []
        while not queue.is_empty():
            got.append(queue.dequeue())

        assert expected == got

    def test_queue_empty(self):
        queue = Queue()

        assert queue.is_empty()

    def test_queue_empty_pop(self):
        queue = Queue()
        with pytest.raises(Exception):
            queue.dequeue()

    def test_stack_peek(self):
        queue = Queue()
        for i in range(1, 6):
            queue.enqueue(i)

        assert queue.peek() == 1
