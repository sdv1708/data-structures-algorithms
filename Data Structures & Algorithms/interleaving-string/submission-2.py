class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        if len(s1) + len(s2) != len(s3):
            return False
            
        memo = {}

        def dfs(i, j): 
            if i + j == len(s3):
                return True 
            
            if (i, j) in memo:
                return memo[(i, j)]

            result = False
            if i < len(s1) and s1[i] == s3[i+j]:
                result = dfs(i + 1, j) 

            if not result and j < len(s2) and s2[j] == s3[i+j]:
                result = dfs(i, j + 1)
            
            memo[(i, j)] = result
            return result
        
        return dfs(0, 0)