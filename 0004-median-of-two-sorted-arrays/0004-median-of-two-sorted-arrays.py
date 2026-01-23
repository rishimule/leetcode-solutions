class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:


        def merge(a1, a2):
            output = []
            l1 = 0
            l2 = 0

            while l1 < len(a1) and l2 < len(a2):
                if a1[l1] <= a2[l2]:
                    output.append(a1[l1])
                    l1 += 1
                else:
                    output.append(a2[l2])
                    l2 += 1
            
            while l1 < len(a1):
                output.append(a1[l1])
                l1 += 1
            
            while l2 < len(a2):
                output.append(a2[l2])
                l2 += 1
            
            return output

        merged_list = merge(nums1, nums2)
        z = len(merged_list)

        if z % 2 == 1:
            return merged_list[z // 2]
        else:
            return (merged_list[(z // 2) - 1] + merged_list[z // 2]) / 2


                
        