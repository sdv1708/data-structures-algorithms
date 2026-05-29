class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxP = 0 
        l = 0
        for r in range(1, len(prices)): 
            if prices[l] > prices[r]: 
                l = r 
            pr = prices[r] - prices[l]
            maxP = max(pr, maxP)
        
        return maxP

        