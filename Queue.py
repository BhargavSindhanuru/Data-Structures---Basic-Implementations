class Queue():
    def __init__(self, head=None):
        self.lst = [head]

    def enqueue(self, new_element):
        self.lst.append(new_element)

    def peek(self):
        return self.lst[0]

    def dequeue(self):
        return self.lst.pop(0)