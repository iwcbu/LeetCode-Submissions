class Solution(object):
    def isPowerOfTwo(self, n):
        """
        :type n: int
        :rtype: bool
        """
        if n == 0:
            return False
        if n == 1:
            return True

        nbin = bin(n)

        if nbin[-1] == '1': # if odd
            return False
        
        nbin = nbin[2:]

        for i in range(1, len(nbin)):
            if nbin[i] == '1':
                return False

        return True 
