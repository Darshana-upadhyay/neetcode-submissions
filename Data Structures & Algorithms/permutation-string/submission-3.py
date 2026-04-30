class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:  
        for i in range(len(s2)-len(s1) + 1):
            window = s2[i:i+len(s1)]
            for j in range(len(s1)):
                if s1[j] in window:
                    window = window.replace(s1[j], "", 1)
                else:
                    break
            if window == "":
                return True
        return False