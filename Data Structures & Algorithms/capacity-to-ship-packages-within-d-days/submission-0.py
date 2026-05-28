class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        l = max(weights) # this is the min the belt must be able to handle 
        r = sum(weights) # this is the maximum set, because it obviously cannot exceed this 
        minC = r # we have to minimize this  

        def canShip(cap): 
            days_taken = 1
            currCap = cap 
            for w in weights:
                if currCap - w < 0: # resetting capacity when we run out of it 
                    days_taken += 1 
                    if days_taken > days: 
                        return False 
                    currCap = cap 

                currCap -= w 
            
            return True 
        
        while l <= r: 
            cap = (l + r) // 2
            if canShip(cap): 
                minC = min(minC, cap)
                r = cap - 1 
            else: 
                l = cap + 1 

        return minC 
        

                 
        