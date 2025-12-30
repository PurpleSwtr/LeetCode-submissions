class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        zeros = []
        pos = 0
        for i, num in enumerate(nums):
            if nums[i] != 0:
                nums[pos] = nums[i]
                pos += 1
        for i in range(pos, len(nums)):
            nums[i] = 0




        
