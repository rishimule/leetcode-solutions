class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])

        q = collections.deque()

        fresh = set()
        m = 0

        visited = set()

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 2:
                    q.append((r, c, m))
                if grid[r][c] == 1:
                    fresh.add((r, c))
        
        
        while q:
            row, col , mr = q.popleft()
            
            directions = [(-1, 0), (0, -1), (1, 0), (0, 1)]

            for dr, dc in directions:
                r = row + dr
                c = col + dc

                if ((r in range(rows))
                    and (c in range(cols))
                    and ((r,c) not in visited)
                    and (grid[r][c] == 1)):

                    # apple is spoiled
                    grid[r][c] = 2
                    q.append((r, c, mr + 1))
                    fresh.remove((r, c))
    
            
            visited.add((row, col))
            m = max(m, mr)

        if len(fresh) > 0:
            return -1
        else:
            return m
        




        
