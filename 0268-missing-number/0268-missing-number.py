class Solution:
    def missingNumber(self, nums: List[int]) -> int:

        n = len(nums)

        totalsum = int(n*(n+1)/2)

        for num in nums:
            totalsum -= num
        
        return totalsum
        