class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        result = []
        def backtrack(index, path): 
            total = sum(path)
            if total == target: 
                result.append(list(path))
                return 
            
            if total > target: 
                return 
            
            for i in range(index, len(nums)): 
                path.append(nums[i])
                backtrack(i, path)
                path.pop()
        
        backtrack(0, [])
        return result