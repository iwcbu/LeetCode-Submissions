class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        if numRows == 1:
            return [[1]]

        dp = [[1], [1,1]]
        for row in range(2, numRows):
            rowCurr = [1]
            rowPrev = dp[row-1]
            for i in range(1, len(rowPrev)):
                rowCurr.append(rowPrev[i-1] + rowPrev[i])
            
            rowCurr.append(1)
            dp.append(rowCurr)
        
        return dp

                



        
