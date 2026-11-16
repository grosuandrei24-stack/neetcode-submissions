from typing import List # this is used to add type hints for List type

def get_sum(nums: List[int]) -> int:
    suma = 0
    for element in nums:
        suma += element
    return suma

def get_min(nums: List[int]) -> int:
    minimum = nums[0]
    for element in nums:
        if element < minimum:
            minimum = element
    return minimum

def get_max(nums: List[int]) -> int:
    maximum = nums[0]
    for element in nums:
        if element > maximum:
            maximum = element
    return maximum

# do not modify below this line
print(get_sum([1, 2, 3, 4, 5]))
print(get_sum([5, 4, 5, 6]))

print(get_min([7, 3, 4, 5]))
print(get_min([5, 4, 5, 6]))

print(get_max([7, 3, 4, 5]))
print(get_max([5, 4, 5, 6]))
