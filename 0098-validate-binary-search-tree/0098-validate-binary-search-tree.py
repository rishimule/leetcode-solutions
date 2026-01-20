# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        
        def dps(node: TreeNode, min, max):
            if node.val > min and node.val < max:
                left = dps(node.left, min, node.val) if node.left else True
                right = dps(node.right, node.val, max) if node.right else True
                return left and right
            return False
        
        return dps(root, float("-inf"), float("inf"))
                