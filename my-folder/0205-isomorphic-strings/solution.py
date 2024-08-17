class Solution(object):
    def isIsomorphic(self, s, t):
        if s == t:
            return True
        
        d = {}
        dvs = set()
        for i in range(len(s)):
            if s[i] not in d:
                if t[i] in dvs:
                    return False
                
                d[s[i]] = t[i]
                dvs.add(t[i])
            elif d[s[i]] != t[i]:
                return False
        
        return True
            
            


                
                
        



        
