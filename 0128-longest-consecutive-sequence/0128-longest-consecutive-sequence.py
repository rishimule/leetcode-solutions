class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numset = set(nums)
        res = 0
        
        for number in numset:
            # We check if its the start of the sequence
            if (number- 1) not in numset:
                lg =1
                while (number + lg) in numset:
                    lg += 1
                res = max(res, lg)
        
        return res
                
                          