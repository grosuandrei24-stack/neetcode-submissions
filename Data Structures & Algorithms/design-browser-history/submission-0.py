class ListNode:
    def __init__(self, val):
        self.val = val
        self.prev = None
        self.next = None

class BrowserHistory:

    def __init__(self, homepage: str):
        nod_nou = ListNode(homepage)
        self.head = nod_nou
        self.tail = nod_nou
        self.pagina_actuala = nod_nou
        
    def visit(self, url: str) -> None:
        #Stergerea istoricului de dupa pagina actuala 
        if self.pagina_actuala.next != None:
            self.pagina_actuala.next.prev = None
        self.pagina_actuala.next = None
        self.tail = self.pagina_actuala
        #Accesarea noii pagini web
        nod_nou = ListNode(url)
        self.tail.next = nod_nou
        nod_nou.prev = self.tail
        self.tail = nod_nou
        self.pagina_actuala = nod_nou

    def back(self, steps: int) -> str:
        index = 0
        while True:
            index += 1
            if self.pagina_actuala.prev != None:
                self.pagina_actuala = self.pagina_actuala.prev
            if index == steps or self.pagina_actuala.prev is None:
                return self.pagina_actuala.val 
        

    def forward(self, steps: int) -> str:
        index = 0
        while True:
            index += 1
            if self.pagina_actuala.next != None:
                self.pagina_actuala = self.pagina_actuala.next
            if index == steps or self.pagina_actuala.next is None:
                return self.pagina_actuala.val


# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)