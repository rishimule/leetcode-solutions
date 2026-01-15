class Solution:
    def maximizeSquareHoleArea(self, n: int, m: int, hBars: List[int], vBars: List[int]) -> int:

        #TODO: null check

        def maxConsecutiveCount(arr):
            numset = set(arr)
            maxStreak = 0

            for num in numset:
                if num-1 not in numset:
                    curr = num
                    count = 1

                    while curr + 1 in numset:
                        count += 1
                        curr += 1

                    maxStreak = max(maxStreak, count)
            
            return maxStreak
        
        size = min(maxConsecutiveCount(hBars), maxConsecutiveCount(vBars)) +1
        return size*size
    
    

        
        