class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [1] * n  # dp[i] = LIS ending exactly at index i

        for i in range(n):              # left to right
            for j in range(i):          # only earlier indices
                if nums[j] < nums[i]:
                    dp[i] = max(dp[i], 1 + dp[j])

        return max(dp)