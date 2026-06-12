class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)

        maxLeftWall = [0] * n
        maxRightWall = [0] * n

        maxLeft = 0
        for i in range(0, n):
            maxLeftWall[i] = maxLeft
            maxLeft = max(maxLeft, height[i])
        
        maxRight = 0
        for i in range(n-1, -1, -1):
            maxRightWall[i] = maxRight
            maxRight = max(maxRight, height[i])
        
        res = 0
        for i in range(n):
            if height[i] < maxLeftWall[i] and height[i] < maxRightWall[i]:
                res += min(maxLeftWall[i], maxRightWall[i])- height[i]
        
        return res

        