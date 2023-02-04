class Stack:

    def __init__(self):
        self.stack = []

    def push(self, data):
        self.stack.append(data)

    def peek(self):
        return self.stack[-1]

    def pop(self):
        if self.size() < 1:
            return None

        data = self.stack[-1]
        del self.stack[-1]

        #self.stack = self.stack[:-1]

        return data

    def is_empty(self):
        return self.stack == []

    def copy(self):
        copy = Stack()
        copy.stack = self.stack.copy()

        return copy

    def size(self):
        return len(self.stack)


def findMax(stack):
    max = 0
    copy = Stack()
    copy.stack = stack.stack.copy()
    max = helper(max, copy)
    return max


def helper(m, stack):
    if stack.is_empty():
        return m
    else:
        i = stack.pop()
        return helper(max(i, m), stack)


# s = Stack()

# s.push(1)
# s.push(2)
# s.push(2)
# s.push(5)
# s.push(3)
# s.push(4)

# print(s.peek())
# print(s.size())


# # print(s.pop())


# print(s.peek())

# print(s.size())

# # print(s.pop())
# # print(s.pop())
# # print(s.pop())
# # print(s.pop())
# # print(s.pop())
# print(findMax(s))
