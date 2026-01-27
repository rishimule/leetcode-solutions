# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        
        # def dfs(node):
        #     if root == None:
        #         return 0
            
        #     l = r = 0

        #     if node.left != None:
        #         l = dfs(node.left)

        #     if node.right != None:
        #         r = dfs(node.right)

        #     return 1 + max(l, r)

        # return dfs(root)

        stack = [(root, 0)]
        maxdepth = 0

        while stack:
            node, depth = stack.pop()

            if node != None:
                depth += 1
                stack.append((node.left, depth))
                stack.append((node.right, depth))
            
            maxdepth = max(maxdepth, depth)
        
        return maxdepth
         
        