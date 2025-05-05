class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n <= 1:
            return 1
        
        a, b = 1, 1 #this represents, dp(i-1) and dp(i-2)
        for i in range(2, n+1):
            a, b = b, a + b
        return b

        

            
            
