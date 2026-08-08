class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        maximum = arr[-1]
        arr[-1] = -1
        for index in range(-2, -len(arr)-1, -1):
            current_element = arr[index]
            arr[index] = maximum
            if current_element > maximum :
                maximum = current_element
        return arr