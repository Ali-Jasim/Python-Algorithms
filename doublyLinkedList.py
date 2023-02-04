class Node:

    def __init__(self, data):
        self.data = data
        self.next = None
        self.previous = None


class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def insert(self, data):
        node = Node(data)

        if self.head is None:
            self.head = node
            self.tail = node
        else:
            self.tail.next = node
            node.previous = self.tail
            self.tail = node

    def insert_end(self, data):
        node = Node(data)

    def traverse_forward(self):
        node = self.head

        while node is not None:
            print(node.data)
            node = node.next

    def traverse_backward(self):
        node = self.tail

        while node is not None:
            print(node.data)
            node = node.previous


if __name__ == '__main__':
    l = DoublyLinkedList()

    l.insert(1)
    l.insert(2)

    l.traverse_forward()
    print('======')
    l.traverse_backward()
