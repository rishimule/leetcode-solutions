class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # TODO: Null checks
        if len(prices) < 2:
            return 0

        # [7,1,5,3,6,4]
        #. l r  

        l = 0
        r = 1

        res = 0

        while r < len(prices):
            if prices[l] < prices[r]:
                profit = prices[r] - prices[l]
                res = max(res, profit)
                r += 1
            else:
                l = r
                r = l+1
        
        return res


            