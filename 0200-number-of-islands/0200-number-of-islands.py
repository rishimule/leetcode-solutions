class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:

        rows, cols = len(grid), len(grid[0])
        islands = 0
        visited = set()

        def bfs(r,c):
            q = collections.deque()
            visited.add((r,c))
            q.append((r,c))
            
            while q:
                row, col = q.popleft()
                nbrs = [[-1, 0], [0,-1], [1, 0], [0,1]]
                for nr, nc in nbrs:
                    r, c = row + nr, col + nc

                    if ((r, c) not in visited and
                        r in range(rows) and
                        c in range(cols) and
                        grid[r][c] == "1"):

                        q.append((r,c))
                        visited.add((r,c))

        for r in range(rows):
            for c in range(cols):
                if ((r,c) not in visited) and (grid[r][c] == "1"):
                    bfs(r, c)
                    islands += 1 
        
        return islands
