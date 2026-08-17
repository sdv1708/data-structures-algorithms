class Solution:
    def lastStoneWeightII(self, stones: List[int]) -> int:
        total = sum(stones)

        target = total // 2 
        n = len(stones)

        dp = [[0] * (target + 1) for _ in range(n + 1)] 



        # dp[i][s] : max weight achievable by using the first i stones upto weight s 
        for i in range(1, n + 1): 
            for s in range(target + 1): 
                if s - stones[i - 1] >= 0: 
                    dp[i][s] = max(dp[i - 1][s], dp[i - 1][s - stones[i - 1]] + stones[i - 1]) 
                else: 
                    dp[i][s] = dp[i - 1][s]
        
        return total - 2 * dp[n][target]
        