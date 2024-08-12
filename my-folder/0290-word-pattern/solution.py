class Solution(object):
    def wordPattern(self, pattern, s):
        string = s.split(" ")
        if len(string) != len(pattern):
            return False

        d = {}
        d2 = {}

        for i in range(len(string)):
            if string[i] not in d and pattern[i] not in d2:
                d[string[i]] = pattern[i]
                d2[pattern[i]] = string[i]
            elif string[i] in d and pattern[i] in d2:
                if d[string[i]] != pattern[i] or d2[pattern[i]] != string[i]:
                    return False
            else:
                return False
        
        return True
        
