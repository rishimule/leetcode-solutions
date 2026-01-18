class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        #TODO: Null checks

        a = cost[0] 
        b = cost[1]
        
        for i in range(2, len(cost)):
            c = min(a, b) + cost[i]
            a, b = b, c
        
        return min(a, b)