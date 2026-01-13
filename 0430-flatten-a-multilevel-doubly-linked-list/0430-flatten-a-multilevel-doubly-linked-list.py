"""
# Definition for a Node.
class Node:
    def __init__(self, val, prev, next, child):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child
"""

class Solution:
    def flatten(self, head: 'Optional[Node]') -> 'Optional[Node]':
        #TODO: null check
        if head == None:
            return head

        prev = None

        stack = []
        stack.append(head)

        while stack:
            node = stack.pop()

            if node.next:
                stack.append(node.next)
            if node.child:
                stack.append(node.child)
                node.child = None

            node.prev = prev
            if prev:
                prev.next = node
            prev = node

        return head
        