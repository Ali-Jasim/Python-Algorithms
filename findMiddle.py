from linkedlist import *


def niave(l):

    count = 0
    node = l.head
    while node is not None:
        count += 1
        node = node.next

    node = l.head
    for i in range(int(count/2)):
        node = node.next

    return node


def better(l):

    p1 = l.head
    p2 = l.head
    count = 0

    while p1 is not None:
        p1 = p1.next
        if count % 2 == 0:
            p2 = p2.next
        count += 1

    return p2


def evenBetter(l):
    fpointer = l.head
    spointer = l.head

    while fpointer is not None and fpointer.next is not None:
        fpointer = fpointer.next.next
        spointer = spointer.next

    return spointer


l = LinkedList()

l.insert(3)
l.insert(4)
l.insert(4)
l.insert(4)
l.insert(1)
l.insert(3)
l.insert(4)
l.insert(4)
l.insert(4)
l.insert(4)

a = evenBetter(l)

l.traverse()

print(a)
