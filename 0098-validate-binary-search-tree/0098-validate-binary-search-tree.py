# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True

        def dfs(node, min, max):
            if node.val > min and node.val < max:

                left = dfs(node.left, min, node.val) if node.left else True

                right = dfs(node.right,  node.val, max) if node.right else True

                return left and right
            
            else:
                return False
            
        return dfs(root, float("-inf"), float("inf"))
        