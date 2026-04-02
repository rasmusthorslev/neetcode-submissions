class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit=0
        min_price = prices[0]
        for i in range(len(prices)):
            if prices[i] < min_price:
                min_price = prices[i]
            profit = max(prices[i]-min_price, profit)
        return profit
        