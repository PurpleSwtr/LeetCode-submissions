class Solution:
    def check_anagram(self, word1: str, word2: str) -> bool:
        if sorted(word1) == sorted(word2):
            return True
        return False

    
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        res = {}
        for word in strs:
            counts = [0] * 26
            for char in word:
                counts[ord(char) - ord("a")] += 1
            key = tuple(counts)
            if key not in res:
                res[key] = []
            res[key].append(word)
        return list(res.values())



    # res = []
    # while (len(strs) > 0):
    #     first = strs.pop()
    #     sublist = []
    #     for i, word in enumerate(sorted(strs)):
    #         for tmp_sub in res:
    #             if self.check_anagram(word, first) and word not in sublist:
    #                 sublist.append(strs.pop(i))
    #             elif self.check_anagram(tmp_sub[0], first):
    #                 tmp_sub.append(first)
    #     sublist.append(first)        
    #     res.append(sublist)
    # return res
