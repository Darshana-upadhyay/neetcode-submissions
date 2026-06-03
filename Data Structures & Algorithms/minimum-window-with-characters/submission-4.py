class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if t == "":
            return ""

        countT, window = Counter(t), {}

        have, need = 0, len(countT)
        res, reslen = [-1,-1], float("infinity")

        l = 0

        for r, ch in enumerate(s):
            window[ch] = 1 + window.get(ch,0)
            if ch in countT and window[ch] == countT[ch]:
                have += 1
            while have == need:
                if r-l+1 < reslen:
                    reslen = r-l+1
                    res = l,r
                window[s[l]] -= 1

                if s[l] in countT and window[s[l]] < countT[s[l]]:
                    have -= 1

                l += 1

            
        l, r = res
        return s[l:r+1] if reslen != float("infinity") else ""




        