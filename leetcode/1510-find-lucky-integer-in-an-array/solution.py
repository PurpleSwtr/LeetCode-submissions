class Solution:
    def findLucky(self, arr: list[int]) -> int:
        lucky = {num: arr.count(num) for num in arr}
        res = []
        for num in set(arr):
            if lucky.get(num) == num:
                res.append(num)
        if res:
            return max(res)
        else:
            return -1
