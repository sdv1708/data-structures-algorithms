class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        result = []
        def backtrack(index, path, remaining): 
    
            if remaining == 0: 
                result.append(list(path))
                return 
            
            if remaining < 0: 
                return 
            
            for i in range(index, len(candidates)): 
                if i > index and candidates[i-1] == candidates[i]: 
                    continue

                path.append(candidates[i])
                backtrack(i+1, path, remaining - candidates[i])
                path.pop()
        
        backtrack(0, [], target)
        return result
        