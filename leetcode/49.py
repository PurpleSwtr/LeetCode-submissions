class Solution:
    def check_anagram(self, word1: str, word2: str) -> bool:
        if sorted(word1) == sorted(word2):
            return True
        return False

    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        res = {}
        while len(strs) > 0:
            first = "".join(sorted(strs.pop()))
            for word in strs:
                word = "".join(sorted(word))
                if word == first:
                    res[first].append(word)
        return list(res.values())


sl = Solution()

inp = ["act", "pots", "tops", "cat", "stop", "hat"]


print(sl.groupAnagrams(inp))
