class Queue:
    def __init__(self):
        self.items = []

    def __getitem__(self, i):
        return self.items[i]

    def is_empty(self):
        return self.items == []

    def enqueue(self, item):
        self.items.insert(0, item)

    def dequeue(self):
        return self.items.pop()

    def size(self):
        return len(self.items)
