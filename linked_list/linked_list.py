class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

    def __repr__(self):
        return self.data


class LinkedList:
    def __init__(self):
        self.head = None

    def __repr__(self):
        node = self.head
        nodeList = []
        while node is not None:
            nodeList.append(node.data)
            node = node.next

        nodeList.append('None')
        return ' -> '.join(str(v) for v in nodeList)

    def __iter__(self):
        if self.head is None:
            return
        node = self.head
        while node is not None:
            yield node
            node = node.next

    # for testing purposes
    def insert_from_list(self, list):
        for x in list:
            self.append(x)

    def append(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return

        curr_node = self.head
        while curr_node.next is not None:
            curr_node = curr_node.next
        curr_node.next = new_node

    def print_list(self):
        curr_node = self.head
        while curr_node is not None:
            print(curr_node.data)
            curr_node = curr_node.next

    def prepend(self, data):
        new_head = Node(data)
        new_head.next = self.head
        self.head = new_head

    def insert_after_node(self, prev_node, data):
        if prev_node is None:
            raise TypeError("prev_node can not be None")

        new_node = Node(data)
        new_node.next = prev_node.next
        prev_node.next = new_node

    def delete_node(self, key):
        if self.head is None:
            raise TypeError("Linkedlist is empty")

        if self.head.data == key:
            self.head = self.head.next
            return

        curr_node = self.head
        while curr_node.next is not None:
            if curr_node.next.data is key:
                curr_node.next = curr_node.next.next
                return
            curr_node = curr_node.next
        raise ValueError(f'Node {key} was not found')

    def delete_node_at_pos(self, pos):
        if pos < 0:
            raise IndexError(f'Index {pos} cannot be negative')
        if pos == 0:
            self.head = self.head.next
            return

        prev_node = self.head

        for i in range(1, pos):
            prev_node = prev_node.next
            if prev_node is None:
                raise IndexError(f'Index {pos} is out of range')

        if prev_node is None or prev_node.next is None:
            raise IndexError(f'Index {pos} is out of range')

        prev_node.next = prev_node.next.next

    def len(self):
        if self.head is None:
            return 0
        length = 0

        for node in self:
            length += 1
            node = node.next

        return length

    def swap(self, key_1, key_2):

        if self.head is None:
            return

        prev_1 = None
        curr_1 = self.head
        while curr_1.data is not key_1:
            prev_1 = curr_1
            curr_1 = curr_1.next
            if curr_1 is None:
                raise ValueError(f'{key_1} is not in the list')

        prev_2 = None
        curr_2 = self.head
        while curr_2.data is not key_2:
            prev_2 = curr_2
            curr_2 = curr_2.next
            if curr_2 is None:
                raise ValueError(f'{key_2} is not in the list')

        # then prev_1 is not head node
        if prev_1 is not None:
            prev_1.next = curr_2
        else:
            self.head = curr_2

        if prev_2 is not None:
            prev_2.next = curr_1
        else:
            self.head = curr_2

        curr_1.next, curr_2.next = curr_2.next, curr_1.next
