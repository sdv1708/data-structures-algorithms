class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        
        total = 0 
        def backtrack(index, curr_xor): 
            nonlocal total
            
            total = total + curr_xor
        
            
            for i in range(index, len(nums)): 
                curr_xor = curr_xor ^ nums[i]
                backtrack(i + 1, curr_xor)
                curr_xor = curr_xor ^ nums[i]

        backtrack(0, 0)
        return total
            
            

