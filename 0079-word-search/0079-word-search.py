class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        ROWS = len(board)
        COLS = len(board[0])

        visited = set()
        
        def dfs(row, col, target):

            if board[row][col] == target[0]:
                if len(target) == 1:      # matched the final character
                    return True

                directions = [(0,1), (1, 0), (0, -1), (-1, 0)]
                visited.add((row,col))

                res = False

                for dr, dc in directions:
                    r = row + dr
                    c = col + dc

                    if (0 <= r < ROWS 
                        and 0 <= c < COLS
                        and (r, c) not in visited):
                        res = res or dfs(r, c, target[1:])
                
                visited.remove((row, col))
                    
                return res
                
            return False
        
        for r in range(ROWS):
            for c in range(COLS):
                if dfs(r, c, word):
                    return True

        return False


            
            


        


        