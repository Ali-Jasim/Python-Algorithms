class Queue:
    # use doubly linked list to make all operations O(1)
    # instead of array
    def __init__(self):
        self.queue = []

    def enqueue(self, data):
        self.queue.append(data)

    def dequeue(self):
        if self.is_empty():
            return None
        data = self.queue[0]
        del self.queue[0]
        return data

    def peek(self):
        return self.queue[0]

    def size(self):
        return len(self.queue)

    def is_empty(self):
        return self.size() == 0


q = Queue()

q.enqueue(1)
q.enqueue(2)
q.enqueue(5)
q.enqueue(3)
q.enqueue(4)

print(q.peek())

print(q.dequeue())
print(q.dequeue())
print(q.dequeue())
print(q.dequeue())
print(q.dequeue())
