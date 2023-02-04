from linkedlist import *


def reverse(l):
    prev = None
    curr = l.head
    next = curr.next

    if next is None:
        return

    while curr is not None:
        next = curr.next
        curr.next = prev
        prev = curr
        curr = next

    l.head = prev


def reverseBad(l):
    new = LinkedList()

    node = l.head

    while node is not None:
        new.insert(node.data)
        node = node.next

    return new


l = LinkedList()

l.insert(4)


l.traverse()

# reverse(l)

reverse(l)

l.traverse()
