from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        min_price = prices[0]
        min_price_index = 0
        max_price = 0
        max_profit = 0

        for i, n in enumerate(prices):
            
            if n < min_price:
                min_price = n
                min_price_index = i
            
            if n > min_price and min_price_index < i:
                max_price = n
            
                profit = max_price - min_price

                if profit > max_profit:
                    max_profit = profit

        return max_profit