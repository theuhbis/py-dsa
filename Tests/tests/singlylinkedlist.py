from pydsa import SinglyLinkedList
import pytest


class TestClass:
    def test_singlylinkedlist_pop_front(self):
        ll = SinglyLinkedList()

        num_list = ["one", "two", "three", "four", "five"]

        for num in num_list:
            ll.insert(num)

        got = []
        while not ll.is_empty():
            got.append(ll.pop_front())

        assert num_list == got

    def test_singlylinkedlist_pop(self):
        ll = SinglyLinkedList()

        num_list = ["one", "two", "three", "four", "five"]

        for num in num_list:
            ll.insert(num)

        got = []
        while not ll.is_empty():
            got.append(ll.pop())

        assert num_list[::-1] == got

    def test_singlylinkedlist_remove(self):
        expected = ["one", "two", "four", "five"]
        ll = SinglyLinkedList()

        num_list = ["one", "two", "three", "four", "five"]

        for num in num_list:
            ll.insert(num)

        ll.remove(2)
        got = []
        while not ll.is_empty():
            got.append(ll.pop_front())

        assert expected == got

    def test_singlylinkedlist_empty(self):
        ll = SinglyLinkedList()
        assert ll.is_empty()

    def test_singlylinkedlist_peek_front(self):
        ll = SinglyLinkedList()

        num_list = ["one", "two", "three", "four", "five"]

        for num in num_list:
            ll.insert(num)

        assert "one" == ll.peek_front()

    def test_singlylinkedlist_reverse(self):
        ll = SinglyLinkedList()

        num_list = ["one", "two", "three", "four", "five"]

        for num in num_list:
            ll.insert(num)

        ll.reverse()

        got = []
        while not ll.is_empty():
            got.append(ll.pop_front())

        assert num_list[::-1] == got

    def test_singlylinkedlist_badinsert(self):
        ll = SinglyLinkedList()
        with pytest.raises(Exception):
            ll.insert()

    def test_singlylinkedlist_badpop(self):
        ll = SinglyLinkedList()
        with pytest.raises(Exception):
            ll.pop()
