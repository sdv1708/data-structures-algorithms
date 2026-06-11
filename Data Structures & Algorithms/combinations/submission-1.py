class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        result = []

        def backtrack(index, path): 
            if len(path) == k:
                result.append(list(path))
                return 
            
            if k - len(path) > (n - index + 1): 
                return 
            
            for num in range(index, n + 1):
                path.append(num)
                backtrack(num + 1, path)
                path.pop()
            
        backtrack(1, [])
        return result
            

                
        