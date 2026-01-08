class Solution:
    def maxArea(self, height: List[int]) -> int:

        n = len(height)

        #greedy
        lp  = 0
        rp = n-1

        maxArea = 0

        while lp < rp:
            currArea = (rp - lp) * min(height[lp], height[rp])
            maxArea = max(maxArea, currArea)

            if height[lp] > height[rp]:
                rp -= 1
            else:
                lp += 1
        
        return maxArea


        