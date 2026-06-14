class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key= lambda i: i[0])

        result= [intervals[0]]

        for start, end in intervals:
            if start <= result[-1][1] and end >= result[-1][1] :
                result[-1][1] = end
            elif start > result[-1][1]:
                result.append([start, end])
        
        return result
        