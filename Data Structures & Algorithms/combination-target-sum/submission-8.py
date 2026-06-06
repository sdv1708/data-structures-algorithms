class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        result = []
        def backtrack(index, remaining, path): 
            
            if remaining == 0: 
                result.append(list(path))
                return 
            
            if remaining < 0: 
                return 
            
            for i in range(index, len(nums)): 
                path.append(nums[i])
                backtrack(i, remaining - nums[i], path)
                path.pop()
        
        backtrack(0, target, [])
        return result