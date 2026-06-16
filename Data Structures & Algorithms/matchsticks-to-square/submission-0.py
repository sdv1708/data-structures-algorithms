class Solution:
    def makesquare(self, matchsticks: List[int]) -> bool:
        total = sum(matchsticks)
        if total % 4 != 0:
            return False
        sides = [0] * 4 
        target = total // 4

        matchsticks.sort(reverse=True)  
        
        def backtrack(i):
            if i == len(matchsticks): 
                return True 

            for side in range(4): 
                if sides[side] + matchsticks[i] <= target: 
                    sides[side] += matchsticks[i]
                    if backtrack(i + 1): 
                        return True 
                    sides[side] -= matchsticks[i]
                
                if sides[side] == 0: 
                    break 
            
            return False 
        
        return backtrack(0)

        