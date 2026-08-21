class StackItem:
    def __init__(self, item, min_below):
        self.item = item
        self.min_below = min(item, min_below)

class MinStack:

    def __init__(self):
        self.items = []

    def push(self, val: int) -> None:
        if not self.items:
            new = StackItem(val, val)
        else:
            new = StackItem(val, self.items[-1].min_below)
        self.items.append(new)

    def pop(self) -> None:
        self.items.pop()

    def top(self) -> int:
        return self.items[-1].item

    def getMin(self) -> int:
        return self.items[-1].min_below
