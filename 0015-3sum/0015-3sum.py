class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        nums.sort() # nLogn
        res = [] 
        n = len(nums)
        
        for i, a in enumerate(nums):
            if i > 0 and a == nums[i-1]:
                continue
            #consider [i+1 ....... n-1]
            l = i+1
            r = n-1

            target = 0 - a

            while l < r:
                if nums[l] + nums[r] < target:
                    l += 1
                elif nums[l] + nums[r] > target:
                    r -= 1
                else:
                    res.append([a, nums[l], nums[r]])
                    l += 1
                    while nums[l] == nums[l-1] and l < r:
                        l += 1
        
        return res

        