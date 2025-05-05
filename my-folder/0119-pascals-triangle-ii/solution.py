class Solution(object):
    def getRow(self, rowIndex):
        """
        :type rowIndex: int
        :rtype: List[int]
        """
        dp = [[1],[1, 1]]
        
        if rowIndex == 0:
            return dp[0]
        if rowIndex == 1:
            return dp[1]

        for row in range(2, rowIndex+1):
            rowC = [1]
            rowP = dp[row-1]
            for i in range(1, len(rowP)):
                rowC.append(rowP[i-1] + rowP[i])
            
            rowC.append(1)
            dp.append(rowC)
        
        return dp[rowIndex]
            



