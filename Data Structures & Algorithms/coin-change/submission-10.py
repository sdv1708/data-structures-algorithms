class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        INF = float('inf')
        dp = [INF] * (amount + 1) 

        dp[0] = 0

        for c in coins:  
            for amt in range(1, amount + 1): 
                if (amt - c) >= 0: 
                    dp[amt] = min(dp[amt], 1 + dp[amt-c])
        
        return dp[amount] if dp[amount] != INF else -1
        