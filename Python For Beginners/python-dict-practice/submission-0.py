from typing import Dict # this adds type hinting for Dict

def count_characters(word: str) -> Dict[str, int]:
    dictionar = {}
    for caracter in word:
        if caracter in dictionar:
            dictionar[caracter] += 1
        else:
            dictionar[caracter] = 1
    return dictionar




# don't modify below this line
print(count_characters("hello"))
print(count_characters("world"))
print(count_characters("hello world"))
print(count_characters("this is a longer sentence"))
