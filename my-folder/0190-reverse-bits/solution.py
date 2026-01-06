class Solution(object):
    def reverseBits(self, n):
        """
        :type n: int
        :rtype: int
        """

        nbin = bin(n)
        nbin = nbin[2:]
        nbin = "0"*(32 - len(nbin)) + nbin
        
        nbinrev = nbin[::-1]

        return int(nbinrev, 2)
        
