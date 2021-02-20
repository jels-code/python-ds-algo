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
        return ' -> '.join(nodeList)

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
            return

        if self.head.data == key:
            self.head = self.head.next
            return

        curr_node = self.head
        while curr_node.next is not None:
            if curr_node.next.data is key:
                curr_node.next = curr_node.next.next
                return
            curr_node = curr_node.next
        #  node not found
