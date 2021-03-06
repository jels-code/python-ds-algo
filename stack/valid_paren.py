from stack import Stack
import math

def is_paren_balanced(input_string):
    stack = Stack()

    mapping = {'{': '}', '[': ']', '(': ')'}

    for c in input_string:
        if c in mapping:
            stack.push(c)
        else:
            if stack.is_empty():
                return False
            openingBrace = stack.pop()
            if c != mapping.get(openingBrace):
                return False

    return stack.is_empty()

def reverse_string(input):
    stack = Stack()
    reversed = ""
    for c in input:
        stack.push(c)
    
    while not stack.is_empty():
        reversed += stack.pop()
    return reversed

def convert_int_to_bin(dec_num):

    binary = ""
    while dec_num > 0:
      remainder = dec_num % 2
      binary += str(int(remainder))
      dec_num = math.floor(dec_num/2)

    return binary[::-1]
