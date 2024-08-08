class Solution(object):
    def longestCommonPrefix(self, strs):
        
        minString = min(strs, key=len)
        result = ""

        for i in range(len(minString)):
            for j in range(len(strs)):
                if strs[j][i] != minString[i] :
                    return result
            result += strs[j][i]
                    
        return result
