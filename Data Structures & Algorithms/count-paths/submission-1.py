class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dp = [[0] * n for _ in range(m)]

        # set all the first row elements to 1
        for j in range(n): 
            dp[0][j] = 1 
        
        # set all the first col elements to 1 
        for i in range(m): 
            dp[i][0] = 1 
        
        # dp[i][j] -> the minimum number of ways we can reach the grid[i][j]
        # constructing the dp array 
        for i in range(1, m):
            for j in range(1, n): 
                dp[i][j] = dp[i-1][j] + dp[i][j-1]
        
        return dp[m-1][n-1]

        