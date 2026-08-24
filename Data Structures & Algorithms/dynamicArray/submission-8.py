class DynamicArray:
    
    def __init__(self, capacity: int):
        self.length = 0
        self.capacity = capacity
        self.array = [0] * self.capacity

    def get(self, i: int) -> int:
        return self.array[i]

    def set(self, i: int, n: int) -> None:
        self.array[i] = n

    def pushback(self, n: int) -> None:
        if self.length >= self.capacity:
            self.resize()
        self.array[self.length] = n
        self.length += 1

    def popback(self) -> int:
        element = self.array[self.length-1]
        self.array[self.length-1] = 0
        self.length -= 1
        return element
 

    def resize(self) -> None:
        #Dublam capacitatea
        self.capacity = 2*self.capacity
        #Facem un vector nou cu capacitate dubla
        array2 = [0] * self.capacity
        #Il updatam cu valorile deja existente
        for index in range(0,self.length):
            array2[index] = self.array[index]
        #Facem ca vectorul initial sa arate spre aceeasi locatie din memorie cu noul vector
        self.array = array2
        


    def getSize(self) -> int:
        return self.length
        
    
    def getCapacity(self) -> int:
        return self.capacity
