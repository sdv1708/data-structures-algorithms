class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        #dp[s] : number of ordered sequences that sum upto exactly s 

        n = len(nums)
        dp = [0] * (target + 1)

        dp[0] = 1 # empty sequence is the only way to sum up to 0 

        # for every s, we need to check if each item works (repeats are ok)
        # so outer loop is the target, inner loop is the num 
        
        for s in range(1, target + 1): 
            for num in nums:
                if s - num >=0 :
                    dp[s] += dp[s - num]
        
        return dp[target]
        
        