class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None


class DoublyLinkedList():
    def __init__(self):
        self.head = None

    def __iter__(self):
        node = self.head
        while node is not None:
            yield node
            node = node.next

    def __repr__(self):
        llist = []
        for node in self:
            llist.append(node.data)
        return ", ".join(llist)

    def append(self, data):
        if self.head is None:
            self.head = Node(data)
            return
        node = self.head
        while node.next is not None:
            node = node.next
        node.next = Node(data)
        node.next.prev = node

    def preprend(self, data):
        new_node = Node(data)
        if self.head is not None:
            self.head.prev = new_node
            new_node.next = self.head
        self.head = new_node

    def add_after_node(self, key, data):
        new_node = Node(data)
        for node in self:
            if node.data is not key:
                continue
            if node.next is None:
                self.append(data)
            else:
                next_node = node.next
                node.next = new_node
                new_node.prev = node
                new_node.next = next_node
                next_node.prev = new_node
            return

    def add_before_node(self, key, data):
        new_node = Node(data)
        for node in self:
            if node.data is not key:
                continue
            if node.prev is None:
                self.preprend(data)
            else:
                next_node = node
                prev_node = node.prev
                prev_node.next = new_node
                new_node.prev = prev_node
                new_node.next = next_node
                next_node.prev = new_node
            return

    def delete(self, key):
        for node in self:
            if node.data is not key:
                continue
            # delete only node
            elif node == self.head and node.next is None:
                self.head = None
            # delete last node
            elif node.next is None:
                node.prev.next = None
            # delete first node
            elif node.prev is None:
                self.head = node.next
                self.head.prev = None
            # delete in between node
            else:
                prev_node = node.prev
                next_node = node.next
                prev_node.next = next_node
                next_node.prev = prev_node
            # delete the node
            node = None
