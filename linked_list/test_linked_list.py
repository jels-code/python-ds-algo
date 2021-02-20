import unittest
from linked_list import LinkedList, Node


class TestStack(unittest.TestCase):

    def test_append(self):
        list = LinkedList()
        list.append('A')
        list.append('B')

        self.assertEqual(repr(list), 'A -> B -> None')

    def test_prepend(self):
        list = LinkedList()
        list.append('B')
        list.prepend('A')

        self.assertEqual(repr(list), 'A -> B -> None')

    def test_insert_after_node(self):
        list = LinkedList()
        list.append('A')
        list.append('C')
        list.insert_after_node(list.head, 'B')

        self.assertEqual(repr(list), 'A -> B -> C -> None')

    def test_delete_node(self):
        list = LinkedList()
        list.append('A')
        list.append('B')

        list.delete_node('non-existent-node')
        self.assertEqual(repr(list), 'A -> B -> None')

        list.delete_node('B')
        self.assertEqual(repr(list), 'A -> None')   

        list.append('B2')
        list.delete_node('A')
        self.assertEqual(repr(list), 'B2 -> None')   

        list.delete_node('B2')
        self.assertEqual(repr(list), 'None')   

        list.delete_node('non-existent-node')
        self.assertIsNone(list.head)


# runs directly without using unittest in command line
if __name__ == '__main__':
    unittest.main()
