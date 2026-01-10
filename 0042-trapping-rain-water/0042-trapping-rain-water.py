class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        leftMax = 0
        rightMax = 0

        left = [0] * n 
        right = [0] * n 
        capacity = [0] * n

        for i in range(0,n):
            left[i] = leftMax
            leftMax = max(height[i], leftMax)

            right[n-i-1] = rightMax
            rightMax = max(height[n-i-1], rightMax)
        
        for i in range(0,n):
            if height[i] < left[i] and height[i] < right[i]:
                capacity[i] = min(left[i], right[i]) - height[i]
        
        return sum(capacity)