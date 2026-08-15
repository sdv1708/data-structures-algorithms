class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])

        dp = [[0] * n for _ in range(m)]

        dp[0][0] = grid[0][0]

        # fill the dp for the first row : previous dp state + grid value 
        for i in range(1, m): 
            dp[i][0] = dp[i - 1][0] + grid[i][0]

        for j in range(1, n): 
            dp[0][j] = dp[0][j - 1] + grid[0][j]
        
        for r in range(1, m): 
            for c in range(1, n): 
                dp[r][c] = grid[r][c] + min(dp[r - 1][c], dp[r][c - 1])
        
        return dp[m - 1][n - 1]
        


        

