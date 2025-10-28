class Solution:
    def hammingWeight(self, n: int) -> int:
        cnt = 0
        b = list(bin(n)[2:])
        for i in b:
            if i == '1':
                cnt += 1
        return cnt
        ...
