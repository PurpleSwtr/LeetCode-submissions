class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        i = 0
        target = 0
        while i < len(haystack):
        # for i, char in enumerate(haystack):
            if haystack[i] == needle[target]:
                if target == (len(needle) - 1):
                    return i - target
                target += 1
            else:
                if target != 0:
                    i = i - target
                target = 0
            i +=1
        return -1
        #     if i < max_len:
        #         if sub == needle[i] and not cont:
        #             memory = i
        #             cont = True
        #         else:
        #             memory = -1
        #             cont = False
        #     else: break
        # return memory


"mississippi"
"missipsippi"
