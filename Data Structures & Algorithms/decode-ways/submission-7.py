class Solution:
    def numDecodings(self, s: str) -> int:
        n = len(s)
        if int(s[0]) == 0:
            return 0 
        dp = [0] * (n + 1) 


        # dp[i] -> number of ways to decode the first i digits 
        dp[0] = 1 # number of ways to decode an empty string 
        dp[1] = 1 # number of ways to decode a single digit, always 1 

        for i in range(2, n + 1):
            # decode one dgit at a time 
            if 1 <= int(s[i-1]) <= 9:
                dp[i] += dp[i-1]
            if 10 <= int(s[i-2:i]) <= 26: 
                dp[i] += dp[i-2]

        return dp[n] 
