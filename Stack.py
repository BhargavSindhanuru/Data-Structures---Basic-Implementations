'''
Implementation of Stack data structure using Linked List
'''

import LinkedList as LL

class Stack():
    def __init__(self, top=None):
        if top:
            obj = LL.Element(top)
            self.ll = LL.LinkedList(obj)
        else:
            self.ll = LL.LinkedList()

    def push(self, new_element):
        obj = LL.Element(new_element)
        obj.next = self.ll.head
        self.ll.head = obj

    def pop(self):
        # Removes the top element from the stack and returns it
        temp = self.ll.head.value
        self.ll.head = self.ll.head.next
        return temp

    def converttoList(self):
        return self.ll.convertToList()[::-1]