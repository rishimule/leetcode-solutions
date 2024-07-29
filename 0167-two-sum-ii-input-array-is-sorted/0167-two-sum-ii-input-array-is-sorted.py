from typing import List


class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        n = len(numbers)
        
        l = 0
        r= n-1
        
        while l<r:
            csum = numbers[l] + numbers[r] 
            if csum == target:
                # remember in this problem indexing starts at 1
                return [l+1, r+1]
            if csum > target:
                r -= 1
            if csum < target:
                l += 1
    

# s = Solution()
# s.twoSum(numbers = [2,7,11,15], target = 9) # Output: [1,2]