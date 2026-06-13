"""
find cycle in nodes
nodes are course
"""

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:

        prereq = {i:[] for i in range(numCourses)}

        for c, p in prerequisites:
            prereq[c].append(p)
       
        visited = set()

        def dfs(crs):
            if prereq[crs] == []:
                return True
            if crs in visited:
                return False

            visited.add(crs)
            for c in prereq[crs]:
                if not dfs(c):
                    return False
            visited.remove(crs)
                
                
            prereq[crs] = []
            return True
                
        for c in range(numCourses):
            if not dfs(c):
                return False
        
        return True

        