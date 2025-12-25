class Solution(object):
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        if x == 0:
            return 0
        if x == 1:
            return 1
        
        temp = 1
        num = 1
        while temp <= x:
            num += 1
            if x / num < num:
                num -= 1
                break
            else:
                temp = num * num
            
        return num
                


        
