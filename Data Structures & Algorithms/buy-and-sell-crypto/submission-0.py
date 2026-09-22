class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        entry_point = 0 

        for i, v in enumerate(prices):
            curr_profit = v - prices[entry_point]
            profit = max(profit, curr_profit)

            if v < prices[entry_point]:
                entry_point = i
        
        return profit