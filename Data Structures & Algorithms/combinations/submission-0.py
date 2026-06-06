class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        result = []

        def backtrack(i, path): 
            if len(path) == k: 
                result.append(list(path))
                return 
            
            if (k - len(path)) > (n - i + 1): # if required elements are greater than the elements available 
                return 
            
            for num in range(i, n+1): 
                path.append(num)
                backtrack(num+1, path)
                path.pop()

        backtrack(1, [])
        return result        