from typing import List


class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        
        def merge(arr:List, l:int , m:int, r:int):
            leftArr  = arr[l:m+1]
            rightArr = arr[m+1:r+1]
            
            li = 0 # Pointer pointing the index in Left array
            ri = 0 # Pointer pointing the index in Right array
            ai = l # Pointer pointing the index in Main array
            
            while li < len(leftArr) and ri < len(rightArr):
                if leftArr[li] <= rightArr[ri]:
                    arr[ai] = leftArr[li]
                    li += 1
                else:
                    arr[ai] = rightArr[ri]
                    ri += 1
                ai += 1
            
            while li < len(leftArr):
                arr[ai] = leftArr[li]
                li += 1
                ai += 1
                
            while ri < len(rightArr):
                arr[ai] = rightArr[ri]
                ri += 1
                ai += 1
            
            
            
        
        def merge_sort(arr:List, l:int, r:int) -> List:
            if l == r:
                return arr
            
            #Find the middle index
            m = (l+r) // 2 
            
            # Recursively call mergesort on each half - Divide Step
            merge_sort(arr, l, m)
            merge_sort(arr, m+1, r)
            
            # Merge step
            merge(arr, l, m, r)
            
            return arr
        
        return merge_sort(nums, 0, len(nums)-1)

# nums = [5,1,1,2,0,0]
# s = Solution()
# s.sortArray(nums)