class Solution:
    def climbStairs(self, n: int) -> int:
        if n <= 1 : 
            return 1 
        
        way_0 = way_1 = 1 

        for i in range(n - 1):  
            temp = way_0 
            way_0 = way_0 + way_1 
            way_1 = temp 
        
        return way_0


        