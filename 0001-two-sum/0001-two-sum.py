"""
[2,3,4,5,6] --- 11

n + diff = target
diff = target - n

[9, 8,  7, 6, ]



"""

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        diffIdx = {}

        for i in range(len(nums)):
            diff = target - nums[i]
            if diff in diffIdx:
                return [diffIdx[diff], i]
            diffIdx[nums[i]] = i
        
        return None
