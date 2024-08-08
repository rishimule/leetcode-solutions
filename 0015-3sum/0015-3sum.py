from typing import List


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # Sort the inputs : O(n^2)
        nums.sort()

        n = len(nums)
        
        res = []
        
        for i in range(n):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            
            a = nums[i]
            bc_sum = 0 - a
            
            # Use two pointer approach for the right side of "a"
            # Initialize left and right pointers
            l = i + 1
            r = n - 1
            
            while l < r:
                if nums[l] + nums[r] > bc_sum:
                    while True:
                        r -= 1
                        if nums[r] != nums[r+1] or l >= r:
                            break
                elif nums[l] + nums[r] < bc_sum:
                    while True:
                        l += 1
                        if nums[l] != nums[l-1] or l >= r:
                            break
                else:
                    res.append([nums[i], nums[l], nums[r]]) # append [a,b,c] to result
                    # check if any other values for "b","c" exist for the current "a"
                    while True:
                        l += 1
                        if nums[l] != nums[l-1] or l >= r:
                            break  
                    while True:
                        r -= 1
                        if nums[r] != nums[r+1] or l >= r:
                            break
            
        return res
            
            
            

# s = Solution()
# s.threeSum(nums = [-1,0,1,2,-1,-4]) # [[-1,-1,2],[-1,0,1]]