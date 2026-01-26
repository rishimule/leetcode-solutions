class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:

        l = 1
        r = max(piles)

        min_rate = r

        # Do binary search    
        while l <= r:
            k = (l+r) // 2
            
            # check for a particulat k
            count = 0
            for p in piles:
                count += math.ceil( p/k)
            
            if count <= h:
                min_rate = min(min_rate, k)
                r = k-1
            else:
                l = k+1
        
        return min_rate

