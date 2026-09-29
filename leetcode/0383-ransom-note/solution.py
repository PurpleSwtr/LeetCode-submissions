from collections import Counter


class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        r_note = Counter(ransomNote)
        mag = Counter(magazine)

        for char, num in r_note.items():
            if mag.get(char, 0) < num:
                return False
        return True

