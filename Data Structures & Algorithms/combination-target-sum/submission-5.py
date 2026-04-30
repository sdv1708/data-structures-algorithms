class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        result = []

        def backtrack(start, total, path): 
            if total == target: 
                result.append(list(path))
                return
            
            if total > target: 
                return 
            
            for i in range(start, len(nums)): 
                path.append(nums[i])
                backtrack(i, total + nums[i], path)
                path.pop()
        
        backtrack(0, 0, [])
        return result



        