class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        n = len(nums)

        minEnd = [0] * n
        maxEnd = [0] * n 

        maxEnd[0] = minEnd[0] = nums[0]

        for i in range(1, n): 
            minEnd[i] = min(nums[i], minEnd[i-1] * nums[i], maxEnd[i-1] * nums[i])
            maxEnd[i] = max(nums[i], minEnd[i-1] * nums[i], maxEnd[i-1] * nums[i])
        
        return max(maxEnd)
        