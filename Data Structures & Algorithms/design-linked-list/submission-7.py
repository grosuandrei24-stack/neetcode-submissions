class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None
        self.prev = None

class MyLinkedList:

    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0

    def get(self, index: int) -> int:
        if index >= self.length:
            return -1
        nod_curent = self.head
        contor = 0
        while nod_curent:
            if contor == index:
                return nod_curent.val
            nod_curent = nod_curent.next
            contor += 1

    def addAtHead(self, val: int) -> None:
        nod_nou = ListNode(val)
        nod_nou.next = self.head
        if self.head:
            self.head.prev = nod_nou
        self.head = nod_nou
        self.length += 1
        if self.length == 1:
            self.tail = nod_nou

    def addAtTail(self, val: int) -> None:
        nod_nou = ListNode(val)
        self.length += 1
        nod_nou.prev = self.tail
        if self.tail:
            self.tail.next = nod_nou
        self.tail = nod_nou
        if self.length == 1:
            self.head = nod_nou
       
    def addAtIndex(self, index: int, val: int) -> None:
        if index == 0:
            self.addAtHead(val)
        elif index == self.length:
            self.addAtTail(val)
        else:
            contor = 0
            nod_curent = self.head
            while nod_curent:
                if contor == index - 1:
                    nod_nou = ListNode(val)
                    element_urmator = nod_curent.next
                    nod_curent.next = nod_nou
                    nod_nou.prev = nod_curent
                    nod_nou.next = element_urmator
                    if element_urmator:
                        element_urmator.prev = nod_nou
                    self.length += 1
                    break
                contor += 1
                nod_curent = nod_curent.next
        

    def deleteAtIndex(self, index: int) -> None:
        if self.length > 0:
            #Stergerea primului element
            if index == 0:
                nod_urmator = self.head.next
                if nod_urmator:
                    nod_urmator.prev = None
                self.head = nod_urmator
                self.length -= 1
            #Stergerea ultimului element
            elif index == self.length - 1:
                nod_precedent = self.tail.prev
                if nod_precedent:
                    nod_precedent.next = None
                self.tail = nod_precedent
                self.length -= 1
            #Stergere din mijloc
            else:
                if 1<=index<self.length:
                    contor = 0
                    nod_curent = self.head
                    while nod_curent:
                        if contor == index:
                            element_precedent = nod_curent.prev
                            element_urmator = nod_curent.next
                            element_precedent.next = element_urmator
                            element_urmator.prev = element_precedent
                            break
                        contor += 1
                        nod_curent = nod_curent.next
                    self.length -= 1




# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)