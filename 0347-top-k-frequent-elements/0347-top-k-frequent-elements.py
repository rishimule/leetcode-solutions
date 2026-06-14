from collections import Counter
import heapq

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        numcounts = Counter(nums)

        h = []
        res = []

        for num, count in numcounts.items():
            heapq.heappush_max(h, (count, num))

        for i in range(k):
            res.append(heapq.heappop_max(h)[1])
        
        return res
        


        