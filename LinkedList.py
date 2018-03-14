class Element():
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList():
    def __init__(self, head = None):
        self.head = head

    def append(self, new_element):
        current = self.head
        if self.head:
            while current.next:
                current = current.next
            current.next = new_element
        else:
            self.head = new_element

    def convertToList(self):
        lst = []
        current = self.head
        if self.head:
            lst.append(current.value)
            while current.next:
                current = current.next
                lst.append(current.value)
        return lst

    def elementAtIndex(self,i):
        # Zero-indexed; negative indices not supported
        ind = 0
        current = self.head
        while current:
            if i == ind:
                return current.value
            current = current.next
            ind += 1
        return None



'''
a = Element(5)
b = Element(10)
c = Element(3)
ll = LinkedList(a)
ll.append(b)
ll.append(c)

print(ll.convertToList())
print(ll.elementAtIndex(2))
print(ll.elementAtIndex(-1))'''