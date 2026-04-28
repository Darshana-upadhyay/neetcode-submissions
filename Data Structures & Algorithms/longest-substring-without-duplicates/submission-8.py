class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        ml = 0
        for i in range(len(s)):
            ls = s[i]
            for j in range (i+1, len(s)):
                if s[j] not in ls:
                    ls += s[j]
                else:
                    break
            ml = max(ml, len(ls))

        return ml
