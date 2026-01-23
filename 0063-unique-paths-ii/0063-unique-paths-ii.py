class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:

        m, n = len(obstacleGrid), len(obstacleGrid[0])

        # Null Check
        if obstacleGrid[m-1][n-1] == 1:
            return 0

        dp = [[0] * n ] * m

        dp[m-1][n-1] = 1

        for row in range(m-1, -1, -1):
            for col in range(n-1, -1, -1):
                # First check if LAST
                if (row == m-1) and (col == n-1):
                    continue

                # Then Check, If obstacle, no path through the cell
                elif obstacleGrid[row][col] == 1:
                    dp[row][col] = 0

                # If all good, update dp    
                else:
                    right = dp[row][col+1] if col+1 < n else 0
                    down = dp[row+1][col] if row+1 < m else 0

                    dp[row][col] = right + down
        
        return dp[0][0]


        