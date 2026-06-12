"""
     .  .  .
   .  .      
.             .
--------------------

but at lowest and sell at highest
"""
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        #edgecase:
        if len(prices) < 2:
            return 0
        
        

        MAX_PRICE = prices[0] 
        MIN_PRICE = prices[0]

        profit = MAX_PRICE - MIN_PRICE

        for p in prices:
            if p > MAX_PRICE:
                #update maxprice
                MAX_PRICE = p
            elif p < MIN_PRICE:
                #update minprice
                MIN_PRICE = p
                #update maxprice
                MAX_PRICE = p
            
            profit = max(profit, MAX_PRICE - MIN_PRICE)
        
        return profit

        