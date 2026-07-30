from collections import Counter
import heapq

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]: 
        heap = []

        for val, count in list(Counter(nums).items()):
            heapq.heappush(heap, (count, val))
            if len(heap) > k:
                heapq.heappop(heap)
        
        res = []
        for count, val in heap:
            res.append(val)
        
        return res


        


        