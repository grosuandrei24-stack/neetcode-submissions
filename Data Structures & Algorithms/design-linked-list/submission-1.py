class ListNode:
    def __init__(self,val):
        self.val = val
        self.next = None

class MyLinkedList:

    def __init__(self):
        self.head = None

    def get(self, index: int) -> int:
        current_node = self.head
        contor = 0
        while current_node:
            if contor == index:
                return current_node.val
            current_node = current_node.next
            contor += 1
        return -1

    def addAtHead(self, val: int) -> None:
        new_node = ListNode(val)
        new_node.next = self.head
        self.head = new_node

    def addAtTail(self, val: int) -> None:
        current_node = self.head
        if current_node:
            while current_node:
                if current_node.next is None:
                    new_node = ListNode(val)
                    current_node.next = new_node
                    break
                current_node = current_node.next
        else:
            self.addAtHead(val)
        

    def addAtIndex(self, index: int, val: int) -> None:
        if index == 0:
            self.addAtHead(val)
        else:
            current_node = self.head
            contor = 0
            while current_node:
                if contor == index - 1:
                    new_node = ListNode(val)
                    next_node = current_node.next
                    current_node.next = new_node
                    new_node.next = next_node
                    break
                contor += 1
                current_node = current_node.next
        

    def deleteAtIndex(self, index: int) -> None:
        contor = 0
        current_node = self.head
        if index == 0:
            if self.head:
                self.head = self.head.next
        else:
            while current_node:
                if contor == index - 1:
                    if current_node.next:
                        current_node.next = current_node.next.next
                        break
                current_node = current_node.next
                contor += 1 
        


# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)