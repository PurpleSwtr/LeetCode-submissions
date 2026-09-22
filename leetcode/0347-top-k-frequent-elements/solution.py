class Solution:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        res = {}
        for num in nums:
            res[num] = res.get(num, 0) + 1
        largest = sorted(res, key=lambda x: res[x], reverse=True)
        return largest[:k]
        

