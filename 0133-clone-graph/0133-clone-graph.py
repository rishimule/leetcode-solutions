"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

from typing import Optional
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        
        if not node:
            return None
        
        nodeDict = {} # ----{node.val : Node}

        def parseNode(node):
            newNode = Node(node.val)
            nodeDict[newNode.val] = newNode

            for n in node.neighbors:
                if n.val not in nodeDict: # parse node before adding
                    neighNode = parseNode(n)
                    newNode.neighbors.append(neighNode)
                else: # Directly add node
                    newNode.neighbors.append(nodeDict[n.val])
            return newNode
        
        return parseNode(node)
'''
{1, 2, 3, 4}

[1, [2, 4]]
[2, [1, 3]]
[3, [2, 4]]
[4, [1, 3]]
'''