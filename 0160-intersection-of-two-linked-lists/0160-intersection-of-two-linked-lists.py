# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        len1 = len2 = 0

        node1=  headA
        while node1:
            len1 += 1
            node1 = node1.next

        node2 =  headB
        while node2:
            len2 += 1
            node2 = node2.next
        
        # keep 2 pointers and increment the longer list pointer by the diff in length
        node1, node2 = headA, headB 
    
        for i in range(abs(len1-len2)):
            if len1 > len2:
                node1 = node1.next
            else:
                node2 = node2.next
        
        while node1 != node2 and node1 and node2:
            node1 = node1.next
            node2 = node2.next
        
        return node1


        

        