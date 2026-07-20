class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total = sum(nums)
        
        if total % 2 != 0: 
            return False 
        target = total // 2 
        n = len(nums)

        dp = [[False] * (target + 1) for _ in range(n + 1)]
        #dp[i][s] : using only the first i elements of nums, 
        # is it possible to pick a subset that adds upto s, choices must be made 

        #dp[i][0] : always True , as a sum of 0 can be made by not picking any elemt 
        for i in range(n + 1): 
            dp[i][0] = True 

        for i in range(1, n + 1): 
            for s in range(1, target + 1): 
                if s - nums[i -1] >= 0: 
                    dp[i][s] = (dp[i - 1][s] or 
                                dp[i - 1][s - nums[i -1]])
                else: 
                    dp[i][s] = dp[i - 1][s]

        return dp[n][target] 



        
        