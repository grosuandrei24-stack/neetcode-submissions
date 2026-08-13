class MyStack:

    def __init__(self):
        self.lista = []

    def push(self, x: int) -> None:
        self.lista.append(x)

    def pop(self) -> int:
        return self.lista.pop()

    def top(self) -> int:
        return self.lista[-1]

    def empty(self) -> bool:
        return True if len(self.lista) == 0 else False
        


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()