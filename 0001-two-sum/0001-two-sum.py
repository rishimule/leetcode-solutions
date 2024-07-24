class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        n = len(nums)
        hmap = {}
        for i in range(n):
            if target - nums[i] in hmap:
                return [hmap[target - nums[i]], i]
            else:
                hmap[nums[i]] = i