def topKFrequent(nums: list[int], k: int) -> list[int]:
    res = {}
    for num in nums:
        res[num] = res.get(num, 0) + 1
    largest = sorted(res, key=lambda x: res[x], reverse=True)
    return largest[:k]


print(topKFrequent(nums=[1, 2, 1, 2, 1, 2, 3, 1, 3, 2], k=2))
# [1,2]
