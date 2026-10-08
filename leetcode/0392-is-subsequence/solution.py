class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        if len(t) < len(s):
            return False
        if len(s) < 1:
            return True
        substr = 0
        for char in t:
            if substr < len(s):
                if char == s[substr]:
                    substr += 1
        return True if substr == len(s) else False
