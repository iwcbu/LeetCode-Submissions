class Solution(object):
    def isIsomorphic(self, s, t):
        if len(s) != len(t):
            return False

        d = {}
        d2 = {}

        for i in range(len(s)):
            x = s[i]
            y = t[i]

            if x not in d and y not in d2:
                d[x] = y
                d2[y] = x
            elif x in d and y in d2:
                if d[x] != y and d2[y] != x:
                    return False
            else:
                return False
        return True

                


        
