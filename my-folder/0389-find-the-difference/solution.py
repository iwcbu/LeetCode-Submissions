class Solution(object):
    def findTheDifference(self, s, t):
        for x in t:
            if x not in s or t.count(x) > s.count(x):
                return x



                                       
                

                

        
