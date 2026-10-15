class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        currSum, maxSum = nums[0], nums[0]

        for i in range(1, len(nums)): 
            currSum = max(currSum + nums[i], nums[i])
            maxSum = max(maxSum, currSum)
        
        return maxSum