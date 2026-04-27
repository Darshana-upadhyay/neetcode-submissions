class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        bp = 0
        minbuy = prices[0]
        for sell in prices:
            bp = max(bp, sell-minbuy)
            minbuy = min(minbuy, sell)
        return bp

