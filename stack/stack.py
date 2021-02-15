"""
Stack
"""


class Stack():
    def __init__(self):
        self.stack = []

    def push(self, element):
        self.stack.append(element)

    def pop(self):
        return self.stack.pop()

    def get_stack(self):
        return self.stack

    def is_empty(self):
        return not self.stack

    def peek(self):
        if not self.is_empty():
            return self.stack[-1]
