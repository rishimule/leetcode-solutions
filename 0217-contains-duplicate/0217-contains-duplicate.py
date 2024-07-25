class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        count = {}
        for n in nums:
            count[n] = 1
        if sum(count.values()) == len(nums):
            return False
        return True