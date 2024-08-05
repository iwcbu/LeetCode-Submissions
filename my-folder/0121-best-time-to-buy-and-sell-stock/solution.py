class Solution(object):
    def maxProfit(self, prices):
        if len(prices) == 0:
            return 0

        minPrice = prices[0]
        maxProfit = 0
        
        for price in prices:
            if price < minPrice:
                minPrice = price
            elif price - minPrice > maxProfit:
                maxProfit = price - minPrice

        return maxProfit
