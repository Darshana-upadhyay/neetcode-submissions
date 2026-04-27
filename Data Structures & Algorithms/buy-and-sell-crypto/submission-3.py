class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        res= list()
        if not prices:
            return 0
        for i in range(len(prices)):
            for j in range(i+1, len(prices)):
                if (prices[j] - prices[i]) > 0:
                    res.append(prices[j] - prices[i])
        return max(res) if res else 0
