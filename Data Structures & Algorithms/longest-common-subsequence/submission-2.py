class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        m, n = len(text1), len(text2)
        # Initialize DP table of size (m+1) x (n+1)
        dp = [[0 for _ in range(n + 1)] for _ in range(m + 1)] 
        
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if text1[i-1] == text2[j-1]:
                    # If characters match, add 1 to the result of previous prefixes
                    dp[i][j] = 1 + dp[i - 1][j - 1]
                else:
                    # If they don't match, take the maximum by skipping one character
                    dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
        
        # Return the bottom-right cell
        return dp[m][n] 
