class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        ROW = len(grid)
        COL = len(grid[0])

        visited = set()
        maxArea = 0

        def bfs(r, c) -> int:
            # TODO
            visited.add((r,c))
            area = 1

            directions = [(1, 0), (-1, 0), (0,1), (0, -1)]
            for dr, dc in directions:
                new_r = r + dr
                new_c = c + dc

                if (0 <= new_r < ROW 
                    and  0 <= new_c < COL 
                    and (new_r, new_c) not in visited 
                    and  grid[new_r][new_c] == 1):
                    
                        area += bfs(new_r, new_c)

            return area

        for r in range(ROW):
            for c in range(COL):
                if (r,c) not in visited and  grid[r][c] == 1:
                    area = bfs(r, c)
                    maxArea = max(maxArea, area)
        
        return maxArea