class Solution:
    def reversePrefix(self, s: str, k: int) -> str:
        if len(s) <= 1:
            return s
        left = 0
        right = k - 1
        s = list(s)
        while left < right:
            s[left], s[right] = s[right], s[left]
            right -= 1
            left += 1
            
        return "".join(s)
