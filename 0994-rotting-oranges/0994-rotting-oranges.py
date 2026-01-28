class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        
        q = deque() # ---> (row, col, time)
        visited = set()
        time = 0

        # find all rotten oranges
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 2:
                    q.append((r, c, time))
        
        # do bfs ->  one level per minute
        while q:
            r, c, time = q.popleft()
            visited.add((r, c))

            neighbors = [(-1, 0), (1, 0), (0, 1), (0, -1)]

            for dr, dc in neighbors:
                new_r = r + dr
                new_c = c + dc
                
                if (0 <= new_r < ROWS  
                    and 0 <= new_c < COLS
                    and grid[new_r][new_c] == 1
                    and (new_r, new_c) not in visited):

                    grid[new_r][new_c] = 2
                    q.append((new_r, new_c, time + 1))
        
        # Check if any fresh orange is left
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1:
                    return -1

        return time


        



        