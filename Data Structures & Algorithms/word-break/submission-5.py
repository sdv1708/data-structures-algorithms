class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        n = len(s)
        dp = [False] * (n + 1)

        # dp[i] : True if prefix s[0:i] is in dict and can be fully segmented, else False 
        dp[0] = True 

        for i in range(1, n+1): 
            for j in range(i): 
                if dp[j] and s[j:i] in wordDict: 
                    dp[i] = True 
                    break 
        
        return dp[n]

