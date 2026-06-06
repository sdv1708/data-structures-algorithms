class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        
        total = 0 
        def backtrack(index, curr_xor): 
            if index == len(nums): 
                return curr_xor
            
            pick = backtrack(index + 1, curr_xor ^ nums[index])
            skip = backtrack(index + 1, curr_xor)

            return pick + skip 

        return backtrack(0, 0)
                

