# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root: return []

        res = []

        q = deque()

        q.append((root, 1))
        prev_depth = 0

        while q:
            node, depth = q.popleft()
            if depth > prev_depth:
                res.append(node.val)
                prev_depth += 1

            if node.right:
                q.append((node.right, depth+1))
            if node.left:
                q.append((node.left, depth+1))

        return res
        