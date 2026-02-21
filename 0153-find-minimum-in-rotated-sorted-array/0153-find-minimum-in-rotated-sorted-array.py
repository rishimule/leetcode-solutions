class Solution:
    def findMin(self, nums: List[int]) -> int:
        n = len(nums)
        l, r = 0, n-1
        while l < r:
            m = (l+r) // 2
            if nums[m] > nums[r]:
                # min in right part
                l = m+1
            else:
                # min in left part
                r = m
        
        return nums[l]
        