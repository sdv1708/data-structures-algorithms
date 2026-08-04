class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)

        if n == 1:
            return nums[0]
        part_1 = nums[:n-1] # 0 to last but one 
        part_2 = nums[1:n] # 1 to last

        return max(self.helper(part_1), self.helper(part_2))
        
        
    def helper(self, nums: List[int]): 
        if not nums: 
            return 0 
        
        n = len(nums)
        if n == 1: 
            return nums[0]
        
        dp = [0] * n 
        dp[0] = nums[0]
        dp[1] = max(nums[0], nums[1])

        for i in range(2, n): 
            dp[i] = max(dp[i-1], nums[i] + dp[i-2])
        
        return dp[-1]