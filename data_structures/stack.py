class Stack:
    def __init__(self):
        self.stack = []

    def __getitem__(self, i):
        return self.stack[i]

    def push(self, item):
        self.stack.append(item)

    def peek(self):
        return self.stack[-1]

    def pop(self):
        return self.stack.pop()

    def size(self):
        return len(self.stack)

    def is_empty(self):
        return self.stack == []
