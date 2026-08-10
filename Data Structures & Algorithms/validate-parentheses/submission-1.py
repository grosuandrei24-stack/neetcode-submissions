class Solution:
    def isValid(self, s: str) -> bool:
        dictionar_corespondenta = {")":"(",
                                    "]":"[",
                                    "}":"{"}
        stack = []
        for element in s:
            if element in dictionar_corespondenta.values():
                stack.append(element)
            else:
                if stack:
                    element_de_comparat = stack.pop()
                    if element_de_comparat != dictionar_corespondenta[element]:
                        return False
                else:
                    return False
        if stack:
            return False
        return True
        

        