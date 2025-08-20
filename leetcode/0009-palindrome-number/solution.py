class Solution:
    def isPalindrome(self, x: int) -> bool:
        strint = str(x)
        r_strint = strint[::-1]
        if strint == r_strint:
            return True
        else:  
            return False
