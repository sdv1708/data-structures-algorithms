class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        n = len(nums)
        total = sum(nums)
        
        # Guard clause: check if the target is mathematically possible
        if (total + target) % 2 != 0 or abs(target) > total:
            return 0
            
        P = (total + target) // 2
        dp = [[0] * (P + 1) for _ in range(n + 1)]
        
        # Base case: 1 way to make a sum of 0 with 0 elements
        dp[0][0] = 1
        
        for i in range(1, n + 1):
            # Crucial: start from 0 to correctly handle 0 elements and 0 values in nums
            for s in range(0, P + 1):
                # Always carry forward the ways from the previous elements
                dp[i][s] = dp[i - 1][s]
                # Crucial: use >= 0 to allow exact matches
                if s - nums[i - 1] >= 0:
                    dp[i][s] += dp[i - 1][s - nums[i - 1]]
                    
        return dp[n][P]