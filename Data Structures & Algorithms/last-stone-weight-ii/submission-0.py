class Solution:
    def lastStoneWeightII(self, stones: List[int]) -> int:
        stoneSum = sum(stones)
        memo = {}
        target = stoneSum // 2 

        def dfs(i, total): 
            if total >= target or i == len(stones):
                # we are getting the difference between |group1 - group2|
                return abs(total - (stoneSum - total))
            
            if (i, total) in memo:
                return memo[(i, total)]
            
            memo[(i, total)] = min(dfs(i + 1, total), dfs(i + 1, total + stones[i]))

            return memo[(i, total)]
        
        return dfs(0, 0)
