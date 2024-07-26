from typing import List


class Solution:
    def longestCycle(self, edges: List[int]) -> int:
        # visited = set()
        # maxcycle = -1 
        # cycle_len= 0
        # i = 0
        # while len(visited) < len( edges):
        #     if i not in visited:
        #         visited.add(i)
        #         next_node = edges[i]
        #         visited.add(next_node)
        #         i = edges[next_node]
        #         print(visited)
        #     elif i == -1:
        #         i += 1
                
        visited = set()
        maxLength = -1
        
        for node in range(len(edges)):
            if node not in visited:
                visited.add(node)
                # print(f"Visited : {node}")
                
                # parse through the nodes until you reach an
                # end or a cycle
                path = [node]
                next_node =  edges[node]
                while next_node != -1 and next_node not in visited:
                    node = next_node
                    visited.add(node)
                    # print(f"Visited : {node}")
                    
                    path.append(node)
                    next_node = edges[node]
                
                # print(f"Path : {path}")
                                
                # if cycle exists: find cycle length
                if next_node != -1 and next_node in path:
                    # iterate through the path until you find
                    # idx of next_node 
                    idx = path.index(next_node)
                    length = len(path) - idx
                    maxLength = max(maxLength, length)
                    # print(f"NewMAx = {maxLength}")
        
        return maxLength


           

# s = Solution()
# s.longestCycle(edges = [2,-1,3,1]) # Output: 3

