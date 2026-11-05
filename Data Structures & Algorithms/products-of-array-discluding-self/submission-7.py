class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        res = [0] * n 
        prefix = 1 
        postfix = 1 

        for i in range(n): 
            res[i] = prefix 
            prefix *= nums[i] 
            
        
        for j in range(n - 1, -1, -1): 
            res[j]*= postfix
            postfix *= nums[j]
            

            
        
        return res
        