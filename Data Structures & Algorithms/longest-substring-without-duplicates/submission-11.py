class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s:
            return 0
        l = 0
        r = 1
        n = len(s)
        ml = 1
        sub = {s[0]}
        while r < n:
            if s[r] not in sub:
                sub.add(s[r])
                r += 1
            else:
                ml = max(ml, len(sub))
                print(ml)
                while s[l]!=s[r]:
                    sub.remove(s[l])
                    l += 1
                sub.remove(s[l])
                l += 1
                sub.add(s[r])
                r += 1
            ml = max(ml, len(sub))
        return ml

