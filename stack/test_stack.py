import unittest
from valid_paren import is_paren_balanced, reverse_string, convert_int_to_bin
from stack import Stack


class TestStack(unittest.TestCase):

    def test_stack(self):
        myStack = Stack()
        myStack.push('A')
        myStack.push('B')
        myStack.push('C')
        self.assertEqual(myStack.stack, ['A', 'B', 'C'])
        self.assertEqual(myStack.pop(), 'C')
        self.assertEqual(myStack.pop(), 'B')
        myStack.push('D')
        self.assertEqual(myStack.stack, ['A', 'D'])
        self.assertFalse(myStack.is_empty())
        myStack.pop()
        myStack.pop()
        self.assertTrue(myStack.is_empty())

    def test_valid_paren(self):
        self.assertTrue(is_paren_balanced('()'))
        self.assertTrue(is_paren_balanced('([]){}'))
        self.assertFalse(is_paren_balanced('([{}(]))'))
        # special case: no ending braces
        self.assertFalse(is_paren_balanced('('))
        # special case: only closing brackes
        self.assertFalse(is_paren_balanced(']]'))
    
    def test_reverse_string(self):
        self.assertEqual(reverse_string("hello"), "hello"[::-1])
        self.assertEqual(reverse_string("Hello World!"), "Hello World!"[::-1])

    def test_convert_int_to_bin(self):
        self.assertEqual(convert_int_to_bin(10), '1010')
        self.assertEqual(convert_int_to_bin(188), '10111100')
        self.assertEqual(convert_int_to_bin(4), '100')

# runs directly without using unittest in command line
if __name__ == '__main__':
    unittest.main()
