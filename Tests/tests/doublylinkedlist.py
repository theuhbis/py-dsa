from pydsa import DoublyLinkedList
import pytest


class TestClass:
    def test_doublylinkedlist_popfront(self):
        ll = DoublyLinkedList()

        num_list = ["one", "two", "three", "four", "five"]

        for num in num_list:
            ll.insert(num)

        got = []
        while not ll.is_empty():
            got.append(ll.pop_front())

        assert num_list == got

    def test_doublylinkedlist_popback(self):
        ll = DoublyLinkedList()

        num_list = ["one", "two", "three", "four", "five"]

        for num in num_list:
            ll.insert(num)

        got = []
        while not ll.is_empty():
            got.append(ll.pop_back())

        assert num_list[::-1] == got

    def test_doublylinkedlist_remove(self):
        expected = ["one", "two", "four", "five"]
        ll = DoublyLinkedList()

        num_list = ["one", "two", "three", "four", "five"]

        for num in num_list:
            ll.insert(num)

        ll.remove(2)
        got = []
        while not ll.is_empty():
            got.append(ll.pop_front())

        assert expected == got

    def test_doublylinkedlist_empty(self):
        ll = DoublyLinkedList()
        assert ll.is_empty()

    def test_doublylinkedlist_peekfront(self):
        ll = DoublyLinkedList()

        num_list = ["one", "two", "three", "four", "five"]

        for num in num_list:
            ll.insert(num)

        assert "one" == ll.peek_front()

    def test_doublylinkedlist_peekback(self):
        ll = DoublyLinkedList()

        num_list = ["one", "two", "three", "four", "five"]

        for num in num_list:
            ll.insert(num)

        assert "five" == ll.peek_back()

    def test_doublylinkedlist_reverse(self):
        ll = DoublyLinkedList()

        num_list = ["one", "two", "three", "four", "five"]

        for num in num_list:
            ll.insert(num)

        ll.reverse()

        got = []
        while not ll.is_empty():
            got.append(ll.pop_front())

        assert num_list[::-1] == got

    def test_doublylinkedlist_badinsert(self):
        ll = DoublyLinkedList()
        with pytest.raises(Exception):
            ll.insert()

    def test_doublylinkedlist_badpop(self):
        ll = DoublyLinkedList()
        with pytest.raises(Exception):
            ll.pop_front()
