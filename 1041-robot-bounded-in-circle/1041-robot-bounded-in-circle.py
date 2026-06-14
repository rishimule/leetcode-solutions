class Solution:
    def isRobotBounded(self, instructions: str) -> bool:
        # change in position
        dx, dy = 0, 1
        X, Y = 0, 0 
       

        for move in instructions:
            if move == "G":
                X += dx
                Y += dy

            elif move == "L":
                dx, dy = -dy, dx
            
            else:
                dx, dy = dy, -dx
        
        return (X, Y) == (0, 0) or (dx, dy) != (0, 1) 
    
        