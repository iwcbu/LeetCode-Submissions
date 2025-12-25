class Solution(object):
    def maximumHappinessSum(self, happiness, k):
        """
        :type happiness: List[int]
        :type k: int
        :rtype: int
        """
        if len(happiness) == 1:
            return happiness[0]
        
        happinessSorted = sorted(happiness)[::-1]
        result = 0

        for i in range(k):
            x = happinessSorted[i] - i
            if x >= 0:
                result += x

        return result
            


