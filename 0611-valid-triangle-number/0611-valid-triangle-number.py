class Solution:
    def triangleNumber(self, nums: List[int]) -> int:
        #TODO: null check

        n= len(nums)
        if n<3:
            return 0

        output = 0

        nums.sort() #O(nlogn)

        for k in range(2, n): # O(n) -> O(n^2)
            i,j = 0, k-1
            while i<j: # O(n)
                if nums[i]+nums[j] > nums[k]:
                    output += (j-i) # all values from (i to j-1: j : k) will satisfy 
                    j -= 1
                else:
                    i += 1

        return output