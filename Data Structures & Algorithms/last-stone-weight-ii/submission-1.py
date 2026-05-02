class Solution:
    def lastStoneWeightII(self, stones: List[int]) -> int:
        memo = {} # {index : total weight}
        sumStones = sum(stones)
        target = sumStones // 2 

        def dfs(i, total): 
            if total >= target or i == len(stones): 
                # total is tota-weight in grp1 and (sumStones - total) is the total-weight of group2 
                return abs(total - (sumStones - total))

            if (i, total) in memo: 
                return memo[(i, total)]
            
            # you either choose to add a stone or not, if you are not adding to grp1 you are obv adding it to grp2
            memo[(i, total)] = min(dfs(i + 1, total), dfs(i + 1, total + stones[i])) 

            return memo[(i, total)]
            

        return dfs(0, 0)