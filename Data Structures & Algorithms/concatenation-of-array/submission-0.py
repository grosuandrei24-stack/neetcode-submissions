class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        lungime = len(nums)*2
        ans = [0]*lungime
        for index,value in enumerate(nums):
            ans[index] = value
            ans[index + lungime//2] = value
        return ans
        
        