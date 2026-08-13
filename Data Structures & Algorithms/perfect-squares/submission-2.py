class Solution:
    def numSquares(self, n: int) -> int:
        # dp[s] : min. number of perfect squared numbers needed to add upto s 
        
        # target is n 
        dp = [21818181] * (n + 1)

        dp[0] = 0 # number of perfect squares to add to 0 is 0 

        for s in range(1, n + 1): 
            for i in range(1, int(math.sqrt(s) + 1)): 
                dp[s] = min(dp[s], dp[s - i*i] + 1)
        
        return dp[n]

        