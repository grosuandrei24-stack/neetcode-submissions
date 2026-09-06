from typing import List

def read_integers() -> List[int]:
    input_initial = input()
    lista = input_initial.split(",")
    for index,valoarea in enumerate(lista):
        lista[index] = int(valoarea)
    return lista

# do not modify the code below
print(read_integers())
print(read_integers())
print(read_integers())
