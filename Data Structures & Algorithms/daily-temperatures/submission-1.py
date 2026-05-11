class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = []
        for i in range(len(temperatures)-1):
            j = i + 1
            while temperatures[i] >= temperatures[j]:
                if j == len(temperatures)-1:
                    j = i
                    break
                j += 1
                
            res.append(j-i)
        if res:
            res.append(0)
        return res   
