class Solution:
    def reverseWords(self, s: str) -> str:
        words = list(s)
        spaces = [index for index, num in enumerate(s) if num == " "]
        spaces.append(len(s))
        i = 0
        left = 0
        right = spaces[0] - 1
        while left < len(s):
            while left <= right:
                words[left], words[right] = words[right], words[left]
                left += 1
                right -= 1
            i += 1
            if i >= len(spaces):
                break  
            left = spaces[i - 1] + 1
            right = spaces[i] - 1
        return "".join(words)

