class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = [0]*len(prices)
        for i in range(0, len(prices)):
            for j in range(i+1, len(prices)):
                profit[i]=max(prices[j]-prices[i],profit[i])
            if i==len(prices)-1:
                return max(max(profit), 0)

                