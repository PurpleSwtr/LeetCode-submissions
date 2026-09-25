import string


class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = (
            s.translate(str.maketrans("", "", string.punctuation))
            .lower()
            .replace(" ", "")
        )
        return s == s[::-1]


sl = Solution()

s = "A man, a plan, a canal: Panama"

print(sl.isPalindrome(s))
