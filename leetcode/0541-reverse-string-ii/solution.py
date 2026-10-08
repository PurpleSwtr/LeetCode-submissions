class Solution:
    def reverseStr(self, s: str, k: int) -> str:
        if len(s) <= 1:
            return s
        s = list(s)
        start = 0
        while start < len(s):
            l = start
            r = min(start + k, len(s)) - 1
            while l < r:
                s[l], s[r] = s[r], s[l]
                l += 1
                r -= 1
            start += 2 * k
        return "".join(s)
