class Node:

    def __init__(self, data):
        self.data = data
        self.next = None

    def __repr__(self):
        return str(self.data)


class LinkedList:

    def __init__(self):
        self.head = None
        self.size = 0

    def insert(self, data):
        self.size += 1
        node = Node(data)

        if self.head is None:
            self.head = node
        else:
            node.next = self.head
            self.head = node

    def insert_end(self, data):
        self.size += 1
        node = Node(data)

        if self.head is None:
            self.head = node
        else:
            n = self.head
            while n.next is not None:
                n = n.next
            n.next = node

    def traverse(self):
        node = self.head

        while node is not None:
            print(node.data)
            node = node.next

    def remove(self, data):
        if self.head is None:
            return

        node = self.head
        prev = None

        while node is not None:
            if node.data == data:
                if prev:
                    prev.next = node.next
                else:
                    self.head = node.next
                return
            prev = node
            node = node.next

    def size(self):
        return self.size
