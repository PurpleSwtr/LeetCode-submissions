class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        nums.sort()
        if len(nums) <= 3:
            return []
        left = nums[0]
        right = nums[-1]
        res = []
        for i, _ in enumerate(nums):
            left += 1
            right -= 1
            sum = nums[i] + nums[left] + nums[right]
            if sum == 0:
                res.append(sorted([nums[i], nums[left], nums[right]]))
            # else:
            # res.append([0, 0, 0])
        return res[::-1]
