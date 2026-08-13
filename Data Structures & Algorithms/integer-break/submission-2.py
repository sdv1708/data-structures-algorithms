class Solution:
    def integerBreak(self, n: int) -> int:
        dp = [0] * (n + 1)
        
        # dp[i] : maximum product that can be achieved by breaking i into 2 or more integers 
        dp[2] = 1 # 1 * 1 
        
        for i in range(3, n + 1): 
            for j in range(1, i): 
                dp[i] = max(j * (i - j), dp[i-j] * j, dp[i])
        
        return dp[n]
        