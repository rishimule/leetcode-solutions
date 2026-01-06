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
        if node == None:
            return None

        nodeDict = {}
        parsednodeset = set()

        def parsenode(node):
            newNode = Node(node.val, [])
            nodeDict[node.val] = newNode
            parsednodeset.add(node.val)

            for n in node.neighbors:
                if n.val not in parsednodeset:
                    neighnode = parsenode(n)
                    newNode.neighbors.append(neighnode)
                else:
                    newNode.neighbors.append(nodeDict[n.val])
            
            return newNode

        return parsenode(node)




    
        