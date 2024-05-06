from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)

        if n < 2:
            return 0

        max_profit = 0 

        for i in range(n-1): # try each window
            for j in range(i+1, n):
                profit = prices[i] - prices[j]
                max_sum = max(max_profit, profit)

        return max_profit 


prices = [2,1,4]

solution = Solution()
print(solution.maxProfit(prices))
