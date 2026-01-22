class Solution:
    def minimumPairRemoval(self, nums: List[int]) -> int:
        res = 0
        ordered = False

        while not ordered:
            ordered = True
            minval = float("inf")
            minidx = -1

            for i in range(len(nums) - 1):
                if nums[i+1] < nums[i]:
                    ordered = False
                if nums[i] + nums[i+1] < minval:
                    minval = nums[i] + nums[i+1]
                    minidx = i
                
            
            if not ordered:
                nums = nums[:minidx] + [minval] + nums[minidx+2:]
                res += 1
        
        return res

            


        