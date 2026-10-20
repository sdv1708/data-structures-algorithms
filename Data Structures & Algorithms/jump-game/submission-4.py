class Solution:
    def canJump(self, nums: List[int]) -> bool:
        i = 0
        n = len(nums)
        # step tracks the farthest index we can currently reach
        step = nums[0] 
        
        while i < n:
            # If the current index is beyond the farthest reachable index, we are stuck
            if i > step:
                return False
                
            # Update the farthest reachable index from the current position
            if i + nums[i] > step:
                step = i + nums[i]
                
            # Check if we can already reach or pass the last index
            if step >= n - 1:
                return True
                
            i += 1  # Check every single index sequentially
            
        return False
        
        