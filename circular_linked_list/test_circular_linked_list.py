import unittest
from circular_linked_list import CircularLinkedList, Node


class TestStringMethods(unittest.TestCase):

    def test_iter(self):
        llist = CircularLinkedList()
        llist.append('A')
        llist.append('B')
        llist.print_list()
        self.assertEqual(llist.to_list(), ['A', 'B'])

    def test_prepend(self):
        llist = CircularLinkedList()
        llist.append('B')
        llist.prepend('A')
        llist.print_list()
        self.assertEqual(llist.to_list(), ['A', 'B'])

    def test_from_list(self):
        llist = CircularLinkedList()
        llist.from_list([1, 2, 3])
        self.assertEqual(llist.to_list(), [1, 2, 3])

    def test_remove(self):
        llist = CircularLinkedList()
        llist.from_list([1, 2, 3, 4, 5])
        llist.remove(3)
        self.assertEqual(llist.to_list(), [1, 2, 4, 5])

    def test_remove_head(self):
        llist = CircularLinkedList()
        llist.from_list([1, 2, 3, 4, 5])
        llist.remove(1)
        self.assertEqual(llist.to_list(), [2, 3, 4, 5])

    def test_remove_last(self):
        llist = CircularLinkedList()
        llist.from_list([1, 2, 3, 4, 5])
        llist.remove(5)
        self.assertEqual(llist.to_list(), [1, 2, 3, 4])

    def test_remove_one_node_list(self):
        llist = CircularLinkedList()
        llist.from_list([1])
        llist.remove(1)
        self.assertEqual(llist.to_list(), [])

    def test_remove_non_existent_node(self):
        llist = CircularLinkedList()
        llist.from_list([1, 2, 3, 4, 5])
        self.assertRaises(ValueError, llist.remove, 6)

    def test_len(self):
        llist = CircularLinkedList()
        self.assertEqual(len(llist), 0)
        llist.from_list([1, 2, 3])
        self.assertEqual(len(llist), 3)
        llist.append(9)
        self.assertEqual(len(llist), 4)

    # def test_split_list(self):
    #     llist = CircularLinkedList()
    #     llist.from_list([1, 2, 3, 4])
    #     a = CircularLinkedList()
    #     b = CircularLinkedList()
    #     llist.split_list(a, b)
    #     self.assertEqual(a.to_list, [1, 2])
    #     self.assertEqual(b.to_list, [3, 4])


if __name__ == '__main__':
    unittest.main()
