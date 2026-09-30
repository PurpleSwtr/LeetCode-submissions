class Solution:
    def singleNumber(self, nums: list[int]) -> int:
        s = 0
        for elem in nums:
            s ^= elem
        return s
    

