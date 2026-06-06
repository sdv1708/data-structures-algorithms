class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        result = []
        def backtrack(index, path): 
            
            result.append(path[:])
            
            for i in range(index, len(nums)): 
                if i > index and nums[i-1] == nums[i]: 
                    continue
                path.append(nums[i])
                backtrack(i + 1, path)
                path.pop()
        
        backtrack(0, [])
        return result
        
