class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:

        # By using merge ------> O(m+n)

        # def merge(a1, a2): # O(m+n)
        #     output = []
        #     l1 = 0
        #     l2 = 0

        #     while l1 < len(a1) and l2 < len(a2):
        #         if a1[l1] <= a2[l2]:
        #             output.append(a1[l1])
        #             l1 += 1
        #         else:
        #             output.append(a2[l2])
        #             l2 += 1
            
        #     while l1 < len(a1):
        #         output.append(a1[l1])
        #         l1 += 1
            
        #     while l2 < len(a2):
        #         output.append(a2[l2])
        #         l2 += 1
            
        #     return output

        # merged_list = merge(nums1, nums2)
        # z = len(merged_list)

        # if z % 2 == 1:
        #     return merged_list[z // 2]
        # else:
        #     return (merged_list[(z // 2) - 1] + merged_list[z // 2]) / 2

        A, B = nums1, nums2

        if len(nums1) > len(nums2):
            B, A = A, B
        
        total = len(nums1)+ len(nums2)
        half = total // 2

        l, r = 0, len(A) - 1

        while True:
            i = (l + r) // 2
            j = half - (i+1) - 1

            Aleft = A[i] if i >= 0 else float("-inf")
            Aright = A[i+1] if (i+1) < len(A) else float("inf")
            Bleft = B[j] if j >= 0 else float("-inf")
            Bright = B[j+1] if (j+1) < len(B) else float("inf") 

            # Correct Partition
            if Aleft <= Bright and Bleft <= Aright:
                # odd
                if total % 2:
                    return min(Aright, Bright)
                # even
                return (max(Aleft, Bleft) + min(Aright, Bright)) / 2
            
            # Incorrect Partition
            elif Aleft > Bright:
                r = i-1
            else:
                l = i+1
