import unittest
from doubly_linked_list import DoublyLinkedList, Node


class TestStringMethods(unittest.TestCase):

    def test_iter(self):
        llist = DoublyLinkedList()
        llist.append('A')
        llist.append('B')
        self.assertEqual(repr(llist), 'A, B')

    def test_prepend(self):
        llist = DoublyLinkedList()
        llist.append('B')
        llist.preprend('A')
        self.assertEqual(repr(llist), 'A, B')

    def test_add_after_node(self):
        llist = DoublyLinkedList()
        llist.append('A')
        llist.append('B')
        llist.append('D')
        llist.add_after_node('B', 'C')
        self.assertEqual(repr(llist), 'A, B, C, D')

    def test_add_after_last_node(self):
        llist = DoublyLinkedList()
        llist.append('A')
        llist.append('B')
        llist.add_after_node('B', 'C')
        self.assertEqual(repr(llist), 'A, B, C')

    def test_add_before_node(self):
        llist = DoublyLinkedList()
        llist.append('A')
        llist.append('B')
        llist.append('D')
        llist.add_before_node('D', 'C')
        self.assertEqual(repr(llist), 'A, B, C, D')

    def test_add_before_first_node(self):
        llist = DoublyLinkedList()
        llist.append('B')
        llist.append('C')
        llist.add_before_node('B', 'A')
        self.assertEqual(repr(llist), 'A, B, C')

    def test_delete_node(self):
        llist = DoublyLinkedList()
        llist.append('A')
        llist.append('B')
        llist.append('C')
        llist.append('D')
        llist.delete('C')
        self.assertEqual(repr(llist), 'A, B, D')

        # delete first node
        llist.delete('A')
        self.assertEqual(repr(llist), 'B, D')

        # delete last node
        llist.delete('D')
        self.assertEqual(repr(llist), 'B')

        # delete only node
        llist.delete('B')


if __name__ == '__main__':
    unittest.main()
