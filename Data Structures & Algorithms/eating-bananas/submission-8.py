class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        
        l = 1 
        r = minK = max(piles)

        while l <= r:
            k = (l + r) // 2 
            totalTime = 0 

            for pile in piles: 
                time = math.ceil(pile / k)
                totalTime += time 
                
            if totalTime <= h:
                minK = min(minK, k)
                r = k - 1 
            else: 
                l = k + 1

        return minK 


        