"""

   1 2 3 4                100        200
------------------------------------------------


"""


class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        num_set = set(nums)
        max_len = 0

        
        for n in num_set:
            if n-1 not in num_set:
                # n is the start of the series:
                # start counting
                count = 0
                while (n + count) in num_set:
                    count += 1

                max_len = max(max_len, count)
                count = 0
            
        return max_len