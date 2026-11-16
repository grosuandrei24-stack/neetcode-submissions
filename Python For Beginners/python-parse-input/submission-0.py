from typing import List

def read_integers() -> List[int]:
    user_input = input()
    list_of_numbers = user_input.split(",")
    return list(map(int, list_of_numbers))

# do not modify the code below
print(read_integers())
print(read_integers())
print(read_integers())
