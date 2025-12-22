class Solution(object):
    def titleToNumber(self, columnTitle):
        """
        :type columnTitle: str
        :rtype: int
        """
        ct_rev = columnTitle[::-1]
        result = 0

        for i in range(len(ct_rev)):
            if i == 0:
                result += ord(ct_rev[i]) - 64
            else:
                result += (ord(ct_rev[i]) - 64) * 26 ** i

        return result
        
