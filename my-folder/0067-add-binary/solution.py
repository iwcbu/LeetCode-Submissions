class Solution:
    def addBinary(self, a: str, b: str) -> str:
        if b == "":
            return a
        
        # convert bin to int
        arev = a[::-1]
        brev = b[::-1]

        aint = 0
        bint = 0
        i = 0
        while ( i < len(a) or i < len(b) ):
            if i < len(a):
                if arev[i] == "1":
                    aint += 2**i
            
            if i < len(b):
                if brev[i] == "1":
                    bint += 2**i
            
            i += 1
            
        # add ints
        resultint = aint + bint

        print(aint, "+", bint, "=", resultint)

        # convert results to bin
        result = format(resultint, 'b')

        return result
            


