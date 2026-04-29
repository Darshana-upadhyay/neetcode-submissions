class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        best = 0
        for i in range(len(s)):
            for keep in set(s):           # try every possible majority char
                temp, d = k, 0
                for j in range(i, len(s)):  # contiguous, only forward
                    if s[j] == keep:
                        d += 1
                    elif temp > 0:
                        temp -= 1
                        d += 1
                    else:
                        break
                best = max(best, d)
        return best


