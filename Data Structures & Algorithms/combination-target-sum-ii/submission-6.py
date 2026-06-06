class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        result = []
        def backtrack(index, path): 
            total = sum(path)
            if total == target: 
                result.append(list(path))
                return 
            
            if total > target: 
                return 
            
            for i in range(index, len(candidates)): 
                if i > index and candidates[i-1] == candidates[i]: 
                    continue

                path.append(candidates[i])
                backtrack(i+1, path)
                path.pop()
        
        backtrack(0, [])
        return result
        