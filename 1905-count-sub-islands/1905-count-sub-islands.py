from typing import List


class Solution:
    def countSubIslands(self, grid1: List[List[int]], grid2: List[List[int]]) -> int:
       
        m = len(grid2)
        n = len(grid2[0])
        
        gc = [["w" for i in range(n)] for j in range(m) ]
        
        def dfs(r,c):
            '''
            returns 1 if sub island exists else returns 0.
            mark the island cells as black
 
            '''
            
            validIsland = True
            stack = [(r,c)]
            
            while stack:
                #pop the top element & make it black
                y,x = stack.pop()
                gc[y][x] = "b"
                
                if validIsland:
                    # check for r,c in grid 1
                    if grid1[y][x] == 0:
                        validIsland = False
                
                
                # Add neighbors to stack
                # (x, y-1)
                if y-1 >= 0 and gc[y-1][x] == "w" and grid2[y-1][x] == 1: 
                    stack.append((y-1,x))
                    gc[y-1][x] = "g"
                
                #(x, y+1)
                if y+1 < m and gc[y+1][x] == "w" and grid2[y+1][x] == 1: 
                    stack.append((y+1,x))
                    gc[y+1][x] = "g"
                
                #(x-1, y)
                if x-1 >= 0 and gc[y][x-1] == "w" and grid2[y][x-1] == 1: 
                    stack.append((y,x-1))
                    gc[y][x-1] = "g"
                
                #(x+1, y)
                if x+1 < n and gc[y][x+1] == "w" and grid2[y][x+1] == 1: 
                    stack.append((y,x+1))
                    gc[y][x+1] = "g"
                        
            return 1 if validIsland else 0
  
        count = 0
        
        for r in range(m):
            for c in range(n):
                if gc[r][c] == "w": #check if unvisited
                    if grid2[r][c] == 1:  # check if its land
                        count += dfs(r,c)
                    # else:
                    #     gc[r][c] = "b"
        
        return count
                         
    

    
    
# S = Solution() 
# S.countSubIslands(  grid1 = [[1,1,1,0,0],[0,1,1,1,1],[0,0,0,0,0],[1,0,0,0,0],[1,1,0,1,1]], 
#                     grid2 = [[1,1,1,0,0],[0,0,1,1,1],[0,1,0,0,0],[1,0,1,1,0],[0,1,0,1,0]])   #output = 3            
                
                
                
                