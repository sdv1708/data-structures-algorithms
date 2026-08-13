class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        n = len(nums)

        total = sum(nums) 
        if total % 2 != 0:
            return False 
        
        target = total // 2 

        #dp[i][s] -> using the first i elements, can we achieve a total of s ? 
        dp = [[False] * (target + 1) for _ in range(n + 1)]

        # base cases dp[i][0] = True we can add upto 0, without considering any elements 
        for i in range(n + 1): 
            dp[i][0] = True 

        for i in range(1, n + 1):
            for s in range(1, target + 1): 
                if s - nums[i-1] >= 0: 
                    dp[i][s] = dp[i-1][s] or dp[i-1][s - nums[i-1]]
                else:
                    dp[i][s] = dp[i-1][s]

        return dp[n][target]


        