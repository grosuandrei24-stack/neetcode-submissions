class Node:
    def __init__(self,val):
        self.val = val
        self.next = None

class LinkedList:
    
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0

    def get(self, index: int) -> int:
        #Verificam daca indexul este valid
        if index >= self.length or index < 0:
            return -1
        #Parcurgem lista de la primul nod
        nod_curent = self.head
        contor = 0
        while contor != index:
            nod_curent = nod_curent.next
            contor+=1
        return nod_curent.val

        

    def insertHead(self, val: int) -> None:
        nod_curent = Node(val)
        nod_curent.next = self.head
        self.head = nod_curent
        self.length += 1
        if self.length == 1:
            self.tail = nod_curent

    def insertTail(self, val: int) -> None:
        #Daca lista este goala inseram la cap
        if self.head is None:
            self.insertHead(val)
        else:
            nod_curent = Node(val)
            self.tail.next = nod_curent
            self.tail = nod_curent
            self.length += 1

    def remove(self, index: int) -> bool:
        #Verificare index
        if index < 0 or index >= self.length:
            return False
        #Scoatem de la head
        if index == 0 :
            self.head = self.head.next
            if self.length == 1:
                self.tail = None
            self.length -= 1
            return True
        if index == self.length - 1:
            nod_curent = self.head
            while nod_curent.next.next is not None:
                nod_curent=nod_curent.next
            nod_curent.next = None
            self.tail = nod_curent
            self.length -= 1
            return True  
        nod_curent = self.head
        contor = 0
        while contor != index:
            nod_precedent = nod_curent
            nod_curent = nod_curent.next
            contor += 1
        nod_precedent.next = nod_curent.next
        self.length -= 1
        return True
        

    def getValues(self) -> List[int]:
        lista = []
        nod_curent = self.head
        while nod_curent is not None:
            lista.append(nod_curent.val)
            nod_curent = nod_curent.next
        return lista
        
