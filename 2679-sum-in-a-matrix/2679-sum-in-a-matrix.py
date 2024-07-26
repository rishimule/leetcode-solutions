from typing import List
import numpy as np

class Solution:
    def matrixSum(self, nums: List[List[int]]) -> int:
        
        nums_rows = len(nums)
        nums_cols = len(nums[0])
        
        result = 0
        
        # function to get index of max value in a
        def argmax(a):
            return max(range(len(a)), key=lambda x : a[x])
        
        # repeat process for number of col in nums times
        for i in range (0, nums_cols):
            currMax = 0
            # get max from each row and append max value to result 
            for j in range (0, nums_rows):
                currMax = max(currMax, nums[j].pop(argmax(nums[j])))
            result += currMax
            
        return result
        
        
        
        
        
# s=Solution()
# s.matrixSum(nums = [[7,2,1],[6,4,2],[6,5,3],[3,2,1]]) #15