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

    def insert(self, new_element, i):
        # Returns 1 for success, -1 if not possible
        if self.head:
            if i == 0:
                new_element.next = self.head
                self.head = new_element
                return 1
            else:
                ind = 0
                current = self.head
                while current:
                    if i == ind + 1:
                        new_element.next = current.next
                        current.next = new_element
                        return 1
                    ind += 1
                    current = current.next
        elif i == 0:
            self.head = new_element
            return 1
        return -1

    def deleteFirstOccurrence(self, value):
        current = self.head
        previous = None
        while current.value != value and current.next:
            previous = current
            current = current.next
        if current.value == value:
            if previous:
                previous.next = current.next
            else:
                self.head = current.next




'''
a = Element(5)
b = Element(10)
c = Element(3)
ll = LinkedList(a)
ll.append(b)
ll.append(c)

print(ll.convertToList())
ll.deleteFirstOccurrence(10)
print(ll.convertToList())'''