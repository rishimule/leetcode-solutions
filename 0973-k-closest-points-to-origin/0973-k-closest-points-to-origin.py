import heapq

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        def dist(x, y):
            return x*x + y*y

        h = []

        for x, y in points:
            heapq.heappush_max(h, (dist(x, y), x, y))
            if len(h) > k:
                heapq.heappop_max(h)
        
        res = [[x[1], x[2]] for x in h]

        return res


        