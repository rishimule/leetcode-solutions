class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        n = len(costs) // 2
        #sorting by difference
        costs.sort(key= lambda x: x[0] - x[1])

        totalCost = 0
        
        # Get Total cost for CityA
        for i in range(n):
            totalCost += costs[i][0]

        # Get Total cost for CityB
        for i in range(n, 2*n ):
            totalCost += costs[i][1]
        
        return totalCost
