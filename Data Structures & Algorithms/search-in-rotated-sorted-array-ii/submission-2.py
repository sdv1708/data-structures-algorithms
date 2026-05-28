class Solution:
    def search(self, nums: list[int], target: int) -> bool:
        l, r = 0, len(nums) - 1 

        while l <= r: 
            m = (l + r) // 2 

            # 1. ALWAYS check for the target first
            if nums[m] == target: 
                return True 

            # 2. Handle the duplicate edge case safely
            if nums[l] == nums[m] and nums[m] == nums[r]: 
                l += 1
                r -= 1
                continue 

            # 3. Left half is sorted
            if nums[l] <= nums[m]: 
                if nums[l] <= target < nums[m]:
                    r = m - 1 
                else: 
                    l = m + 1 
            
            # 4. Right half is sorted
            else: 
                if nums[m] < target <= nums[r]:
                    l = m + 1 
                else: 
                    r = m - 1 

        return False