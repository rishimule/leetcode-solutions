class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        h = []

        for i in arr:
            dist = abs(x-i)
            heapq.heappush(h, (dist, i))

        resh = []

        for j in range(k):
            d, i = heapq.heappop(h)
            heapq.heappush(resh, i)

        return [heapq.heappop(resh) for i in range(k)]