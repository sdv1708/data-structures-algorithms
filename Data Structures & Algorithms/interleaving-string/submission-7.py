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

            flag = False 
            # this flag is used to check and update the state 
            # if the remaining suffix s1[i:] and s2[j:] can interleave to form s3[i+j:]

            if i < len(s1) and s1[i] == s3[i+j]:
                flag = dfs(i + 1, j)

            if j < len(s2) and s2[j] == s3[i + j]: 
                flag = dfs(i, j + 1)
            
            memo[(i, j)] = flag 
            return memo[(i, j)]
        
        return dfs(0, 0)
        