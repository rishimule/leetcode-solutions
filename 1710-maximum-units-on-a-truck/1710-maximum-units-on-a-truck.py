class Solution:
    def maximumUnits(self, boxTypes: List[List[int]], truckSize: int) -> int:
        
        boxTypes.sort(key = lambda i : i[1])
        units = 0
        capacity = truckSize

        while capacity > 0 and boxTypes:
            n, u = boxTypes.pop()
            if n < capacity:
                units += n * u
                capacity -= n
            else:
                units += capacity * u
                return units
        
        return units
        



        