from typing import List


class Solution:
    def maxSumAfterPartitioning(self, arr: List[int], k: int) -> int:
        n = len(arr)
        
        # create a dp array of size n+1
        dp = [0 for _ in range (n+1)]
        
        for i in range (1,n+1):
            for j in range (1, k+1):
                if i-j>= 0:
                    # update dp[i] if new max found
                    dp[i] = max(dp[i],dp[i-j]+max(arr[i-j:i])*j)
        return dp[n]
                
            
        
    

# s=Solution()
# s.maxSumAfterPartitioning(arr = [1,4,1,5,7,3,6,1,9,9,3], k = 4) # 83