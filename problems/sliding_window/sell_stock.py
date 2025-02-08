from typing import List
"""
input array stock[i] where i is the price of a stock on the i'th day
need to choose the best time to buy and sell
can also choose not to buy or sell if a profit of zero is the max
"""

# Input: prices = [10,1,5,6,7,1]
# Search criteria buy = low and sell = high = search for the lowest buy and highest val combination


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # window coords
        buy = 0 
        sell = 0
        best_diff = 0

        for i in range(0,len(prices)):
            # check prices[i] against buy position to see if better diff
            profit = prices[i] - prices[buy]
            if profit > best_diff:
                best_diff = profit
                sell = i
            elif profit < 0:
                buy = i
        return best_diff
    
Solution().maxProfit([10,1,5,6,7,1])