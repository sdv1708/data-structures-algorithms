class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # pointers for the 3 segments l, r for (0 and 2)
        # i will traverse through the entire nums array 
        l, r = 0, len(nums) - 1 # everything before l is a 0 and everything after r is a 2  
        i = 0 

        while i <= r: 
            if nums[i] == 0: 
                nums[i], nums[l] = nums[l], nums[i]
                l += 1 
            elif nums[i] == 2: 
                nums[i], nums[r] = nums[r], nums[i]
                r -= 1 
                i -= 1 
            i += 1 
        
