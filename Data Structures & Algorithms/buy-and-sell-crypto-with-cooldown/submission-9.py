class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)

        hold = [0] * n # basically tracks the current value of the stock you own   
        sold = [0] * n 
        cooldown = [0] * n 

        hold[0] = -prices[0]

        for i in range(1, n): 
            hold[i] = max(hold[i-1], cooldown[i-1] - prices[i])
            cooldown[i] = max(cooldown[i-1], sold[i-1])
            sold[i] = hold[i-1] + prices[i]
        
        return max(sold[-1], cooldown[-1])

        