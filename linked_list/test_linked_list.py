import unittest
from linked_list import LinkedList, Node


class TestStack(unittest.TestCase):

    def test_iter(self):
        llist = LinkedList()
        llist.insert_from_list(['A', 'A', 'A'])
        count = 0
        for node in llist:
            self.assertEqual(node.data, 'A')
            count += 1
        self.assertEqual(count, 3)

    def test_append(self):
        llist = LinkedList()
        llist.append('A')
        llist.append('B')

        self.assertEqual(repr(llist), 'A -> B -> None')

    def test_prepend(self):
        llist = LinkedList()
        llist.append('B')

        llist.prepend('A')
        self.assertEqual(repr(llist), 'A -> B -> None')

    def test_insert_after_node(self):
        llist = LinkedList()
        llist.insert_from_list(['A', 'C', 'D', 'E'])

        llist.insert_after_node(llist.head, 'B')
        self.assertEqual(repr(llist), 'A -> B -> C -> D -> E -> None')

    def test_delete_node(self):
        llist = LinkedList()
        llist.insert_from_list(['A', 'B'])

        self.assertRaises(ValueError, llist.delete_node, 'non-existent-node')

        llist.delete_node('B')
        self.assertEqual(repr(llist), 'A -> None')

        llist.append('B2')
        llist.delete_node('A')
        self.assertEqual(repr(llist), 'B2 -> None')

        llist.delete_node('B2')
        self.assertEqual(repr(llist), 'None')

        self.assertRaises(TypeError, llist.delete_node, 'non-existent-node')

    def test_delete_node_at_pos(self):
        llist = LinkedList()
        llist.insert_from_list([0, 1, 2, 3])
        llist.delete_node_at_pos(2)

        self.assertEqual(repr(llist), '0 -> 1 -> 3 -> None')

        self.assertRaises(IndexError, llist.delete_node_at_pos, 3)
        self.assertRaises(IndexError, llist.delete_node_at_pos, -2)
        self.assertRaises(IndexError, llist.delete_node_at_pos, 10)

    def test_len(self):
        llist = LinkedList()
        llist.insert_from_list([0, 1, 2, 3, 4])

        self.assertEqual(llist.len(), 5)

    def test_len_zero(self):
        llist = LinkedList()
        self.assertEqual(llist.len(), 0)

    def test_swap(self):
        llist = LinkedList()
        llist.insert_from_list(['A', 'B', 'C', 'D', 'E'])
        llist.swap('B', 'D')
        self.assertEqual(repr(llist), 'A -> D -> C -> B -> E -> None')

    def test_reverse(self):
        llist = LinkedList()
        llist.insert_from_list(['A', 'B', 'C', 'D', 'E'])
        llist.reverse()
        self.assertEqual(repr(llist), 'E -> D -> C -> B -> A -> None')

    def test_reverse_recursive(self):
        llist = LinkedList()
        llist.insert_from_list(['A', 'B', 'C', 'D', 'E'])

        llist.reverse_recursive()
        self.assertEqual(repr(llist), 'E -> D -> C -> B -> A -> None')

    def test_merge_sorted_lists(self):
        llist = LinkedList()
        llist.insert_from_list([1, 3, 4])
        otherllist = LinkedList()
        otherllist.insert_from_list([2, 4, 7, 8])

        llist.merge_sorted_lists(otherllist)
        self.assertEqual(repr(llist), '1 -> 2 -> 3 -> 4 -> 4 -> 7 -> 8 -> None')

    def test_remove_duplicates(self):
        llist = LinkedList()
        llist.insert_from_list([1, 1, 5, 1, 3, 5])
        llist.remove_duplicates()
        self.assertEqual(repr(llist), '1 -> 5 -> 3 -> None')

    def test_nth_last_node(self):
        llist = LinkedList()
        llist.insert_from_list(['A', 'B', 'C', 'D', 'E'])

        self.assertEqual(llist.nth_to_last(4), 'B')



# runs directly without using unittest in command line
if __name__ == '__main__':
    unittest.main()
