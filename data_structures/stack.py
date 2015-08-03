class Stack:
    def __init__(self):
        self.items = []

    def __getitem__(self, i):
        return self.items[i]

    def push(self, item):
        self.items.append(item)

    def peek(self):
        return self.items[-1]

    def pop(self):
        return self.items.pop()

    def size(self):
        return len(self.items)

    def is_empty(self):
        return self.items == []
