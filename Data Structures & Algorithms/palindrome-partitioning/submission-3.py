class Solution:
    def partition(self, s: str) -> List[List[str]]:

        result = []
        def backtrack(start, path): 
            if start == len(s): 
                result.append(list(path))
                return 
            
            for end in range(start, len(s)): 
                substr = s[start:end+1]
                if substr == substr[::-1]:
                    path.append(substr) 
                    backtrack(end + 1, path)
                    path.pop()
            
        backtrack(0, [])
        return result
        