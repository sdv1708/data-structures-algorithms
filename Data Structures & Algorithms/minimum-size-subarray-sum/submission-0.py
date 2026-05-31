class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        l = 0
        totalSum = 0
        minLen = float('inf') 

        for r in range(len(nums)):
            totalSum += nums[r]
            
            # Shrink the window from the left while the target is met
            while totalSum >= target:
                minLen = min(minLen, r - l + 1)
                totalSum -= nums[l]
                l += 1
                

        return minLen if minLen != float('inf') else 0