import math


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class CircularLinkedList:
    def __init__(self):
        self.head = None

    def __iter__(self):
        if not self.head:
            return

        node = self.head.next
        head = self.head
        yield head

        while node is not head:
            yield node
            node = node.next

    def __repr__(self):
        list = self.to_list()
        return " -> ".join(list)

    def __len__(self):
        count = 0
        for node in self:
            count += 1
        return count

    def to_list(self):
        list = []
        for node in self:
            list.append(node.data)
        return list

    def from_list(self, items):

        if not items:
            return

        self.head = Node(items[0])
        node = self.head
        for i in range(1, len(items)):
            node.next = Node(items[i])
            node = node.next

        node.next = self.head

    def prepend(self, data):
        new_node = Node(data)
        new_node.next = self.head

        if self.head is None:
            new_node.next = new_node
        else:
            node = self.head
            while node.next != self.head:
                node = node.next
            node.next = new_node
        self.head = new_node

    def append(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            self.head.next = self.head
            return

        node = self.head
        while node.next is not self.head:
            node = node.next
        node.next = new_node
        node.next.next = self.head

    def print_list(self):
        print(repr(self))

    def remove(self, key):
        """Removes first instance of key in list"""

        if self.head is None:
            return

        if self.head.next is self.head:
            if self.head.data == key:
                self.head = None
            return

        # now we can assume linked list has at least 2 elements
        if self.head.data == key:
            head = self.head
            self.head = self.head.next
            self.remove(head.data)
            return

        node = self.head
        while node.next.data != key and node.next != self.head:
            node = node.next

        if node.next.data == key:
            node.next = node.next.next
        elif node.next == self.head:
            raise ValueError(f'{key} was not found in the list')

    def split_list(self, a, b):
        """ 
        Returns 2 lists `a` and `b`, formed by splitting the original list from the middle 
        If the list is uneven, `a` will have an extra node
        """

        node = self.head
        for i in range(1, math.ceil(len(self)/2)):
            node = node.next

        b_head = node.next
        node.next = self.head
        a.head = self.head

        node = b_head
        while node.next != self.head:
            node = node.next
        node.next = b_head
        b.head = b_head
