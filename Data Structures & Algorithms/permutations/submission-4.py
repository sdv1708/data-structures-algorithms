class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        result = []

        def backtrack(visited, path): 
            if len(path) == len(nums): 
                result.append(list(path))
                return 
            
            for num in nums:
                if num in visited: 
                    continue 
                visited.add(num)
                path.append(num)
                
                backtrack(visited, path)
                
                path.pop()
                visited.remove(num)

        visited = set()    
        backtrack(visited, [])
        return result

        