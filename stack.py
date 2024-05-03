
class Stack:
    def __init__(self):
        self.stack = []

    def is_empty(self):
        return self.size() == 0

    def size(self):
        return len(self.stack)

    def pop(self):
        if self.is_empty():
            return None
        removed = self.stack.pop()
        return removed

    def peek(self):
        if self.is_empty():
            return None
        last = self.stack.get(self.size() - 1)
        return last

    def push(self, item):
        self.stack.append(item)