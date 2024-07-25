from typing import List
from collections import defaultdict


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        # Create a hashmap to store the number of occurrences
        count = defaultdict(int)
        
        for n in nums:
            count[n] += 1
        
        # Return k elements with max counts
        res = list(count.items())
        res.sort(key=lambda a: a[1], reverse=True)
        print(res)
        
        return [x[0] for x in res[:k]]
            
            
# s = Solution()
# s.topKFrequent(nums = [4,1,-1,2,-1,2,3], k = 2)