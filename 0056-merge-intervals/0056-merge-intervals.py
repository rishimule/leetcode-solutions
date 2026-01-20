class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key= lambda i : i[0]) #O(nLogn)

        output =[ intervals[0] ]

        for start, end in intervals: # O(n)
            lastEnd = output[-1][1]

            if start <= lastEnd:
                output[-1][1] = max(lastEnd, end) # [1,5], [2,3] -> [1,5]
            else:
                output.append([start, end])
        
        return output

        