from typing import List


class Solution:
    def longestCycle(self, edges: List[int]) -> int:

        visited = set()
        maxLength = -1
        
        for node in range(len(edges)):
            if node not in visited:
                visited.add(node)
                
                # parse through the nodes until you reach an
                # end or a cycle
                path = [node]
                next_node =  edges[node]
                while next_node != -1 and next_node not in visited:
                    node = next_node
                    visited.add(node)
                    
                    path.append(node)
                    next_node = edges[node]
                                
                # if cycle exists: find cycle length
                if next_node != -1 and next_node in path:
                    # iterate through the path until you find
                    # idx of next_node 
                    idx = path.index(next_node)
                    length = len(path) - idx
                    maxLength = max(maxLength, length)
        
        return maxLength


           

# s = Solution()
# s.longestCycle(edges = [2,-1,3,1]) # Output: 3

