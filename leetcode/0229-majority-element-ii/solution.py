from collections import Counter

class Solution:
    def majorityElement(self, nums: list[int]) -> list[int]:
        threshold = len(nums) // 3
        counts = Counter(nums)
        return [num for num, freq in counts.items() if freq > threshold]
