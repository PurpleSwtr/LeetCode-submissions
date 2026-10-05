class Solution:
    def sortArrayByParity(self, nums: list[int]) -> list[int]:
        if len(nums) == 1:
            return nums
        left = 0
        right = len(nums) - 1 
        while left < right:
            if nums[left] % 2 == 0:
                left += 1
            elif nums[right] % 2 != 0:
                right -= 1
            else:    
                nums[right], nums[left] = nums[left], nums[right]
                left += 1
                right -= 1
        return nums

