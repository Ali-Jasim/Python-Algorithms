from stack import *


class Queue:

    def __init__(self):
        self.enqueueStack = Stack()
        self.dequeueStack = Stack()

    def enqueue(self, data):
        self.enqueueStack.push(data)

    def dequeue(self):

        if self.dequeueStack.is_empty():

            while not self.enqueueStack.is_empty():
                self.dequeueStack.push(self.enqueueStack.pop())

        return self.dequeueStack.pop()

    def peek(self):
        s2 = self.stack.copy()
        val = None

        while not s2.is_empty():
            val = self.s2.pop()

        return val


a = Queue()

a.enqueue(1)
a.enqueue(2)
a.enqueue(3)
a.enqueue(4)

print(a.dequeue())
print(a.dequeue())
print(a.dequeue())
print(a.dequeue())
print(a.dequeue())
