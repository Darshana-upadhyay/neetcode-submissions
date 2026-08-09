class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        res = 0
        if not prices:
            return 0
        n = len(prices)
        minr = [float('infinity')] * n
        for i in range(1,n):
            minr[i] = min(minr[i-1],prices[i-1])

        for i in range(1,len(prices)):
            res = max(res, prices[i]-minr[i])
        return res
