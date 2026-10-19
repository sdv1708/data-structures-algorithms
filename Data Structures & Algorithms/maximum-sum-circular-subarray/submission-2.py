from typing import List

class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        # Initialize everything with the first element
        globalMax = globalMin = nums[0]
        currMax = currMin = nums[0]
        total = nums[0]
        
        # Iterate from the second element onward
        for i in range(1, len(nums)):
            total += nums[i]
            
            # Kadane's algorithm for Maximum Subarray
            currMax = max(nums[i], currMax + nums[i])
            globalMax = max(globalMax, currMax)
            
            # Kadane's algorithm for Minimum Subarray
            currMin = min(nums[i], currMin + nums[i])
            globalMin = min(globalMin, currMin)
            
        # Edge Case: If all elements are negative, globalMax is the correct answer
        if globalMax < 0:
            return globalMax
            
        # Return the max of non-circular or circular wrapping subarray
        return max(globalMax, total - globalMin)
