class Stack:

    def __init__(self):
        self.stack = []
        self.m = []

    def push(self, data):
        self.stack.append(data)

        if len(self.stack) <= 1:
            self.m.append(data)
            return

        self.m.append(max(data, self.m[-1]))

        # if data > self.m[-1]:
        #     self.m.append(data)
        # else:
        #     self.m.append(self.m[-1])

    def peek(self):
        return self.stack[-1]

    def pop(self):
        if self.size() < 1:
            return None

        data = self.stack[-1]
        self.m.pop()
        del self.stack[-1]

        #self.stack = self.stack[:-1]

        return data

    def max(self):
        return self.m[-1]

    def is_empty(self):
        return self.stack == []

    def size(self):
        return len(self.stack)


s = Stack()

s.push(1)
s.push(2)
s.push(2)
s.push(5)
s.push(3)
s.push(4)


# print(s.pop())


# print(s.pop())
# print(s.pop())
# print(s.pop())
# print(s.pop())
# print(s.pop())
print(s.max())
