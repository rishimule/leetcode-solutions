# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if root is None:
            return []
        
        res = [] # [[3] [9, 20] [15, 7]]

        q = deque() # [ ]    (7, 2)
        q.append((root, 0))
        curr_level = -1 # 2

        while q:
            # pop off and add its children
            node, level = q.popleft()

            if node.left:
                q.append((node.left, level+1))
            if node.right:
                q.append((node.right, level+1))
            
            if  level > curr_level:
                res.append([node.val])
                curr_level += 1
            else:
                res[-1].append(node.val)
    
        return res
            


        