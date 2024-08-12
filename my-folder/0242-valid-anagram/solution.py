class Solution(object):
    def isAnagram(self, s, t):
        if len(s) != len(t):
            return False
        
        s_set, t_set = set(s), set(t)

        if s_set != t_set:
            return False

        for x in s_set :
            if s.count(x) != t.count(x):
                return False
        
        return True
        
        
