import unittest
from linked_list import LinkedList, Node


class TestStack(unittest.TestCase):

    def test_iter(self):
        list = LinkedList()
        list.insert_from_list(['A', 'A', 'A'])
        count = 0
        for node in list:
            self.assertEqual(node.data, 'A')
            count += 1
        self.assertEqual(count, 3)

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
        list.insert_from_list(['A', 'C', 'D', 'E'])

        list.insert_after_node(list.head, 'B')
        self.assertEqual(repr(list), 'A -> B -> C -> D -> E -> None')

    def test_delete_node(self):
        list = LinkedList()
        list.insert_from_list(['A', 'B'])

        self.assertRaises(ValueError, list.delete_node, 'non-existent-node')

        list.delete_node('B')
        self.assertEqual(repr(list), 'A -> None')

        list.append('B2')
        list.delete_node('A')
        self.assertEqual(repr(list), 'B2 -> None')

        list.delete_node('B2')
        self.assertEqual(repr(list), 'None')

        self.assertRaises(TypeError, list.delete_node, 'non-existent-node')

    def test_delete_node_at_pos(self):
        list = LinkedList()
        list.insert_from_list([0, 1, 2, 3])
        list.delete_node_at_pos(2)

        self.assertEqual(repr(list), '0 -> 1 -> 3 -> None')

        self.assertRaises(IndexError, list.delete_node_at_pos, 3)
        self.assertRaises(IndexError, list.delete_node_at_pos, -2)
        self.assertRaises(IndexError, list.delete_node_at_pos, 10)

    def test_len(self):
        list = LinkedList()
        list.insert_from_list([0, 1, 2, 3, 4])

        self.assertEqual(list.len(), 5)

    def test_len_zero(self):
        list = LinkedList()
        self.assertEqual(list.len(), 0)

    def test_swap(self):
        list = LinkedList()
        list.insert_from_list(['A', 'B', 'C', 'D', 'E'])
        list.swap('B', 'D')
        self.assertEqual(repr(list), 'A -> D -> C -> B -> E -> None')

    def test_reverse(self):
        list = LinkedList()
        list.insert_from_list(['A', 'B', 'C', 'D', 'E'])
        list.reverse()
        self.assertEqual(repr(list), 'E -> D -> C -> B -> A -> None')



# runs directly without using unittest in command line
if __name__ == '__main__':
    unittest.main()
