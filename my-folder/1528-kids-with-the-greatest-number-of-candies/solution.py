class Solution(object):
    def kidsWithCandies(self, candies, extraCandies):

        maxi = max(candies)
        result = []
        for x in candies:
            if maxi <= x + extraCandies:
                result += [True]
            else:
                result += [False]

        return result
            

            
        

        
