class Solution(object):
    def strStr(self, haystack, needle):
        if needle not in haystack:
            return -1

        x = len(needle) - 1
        y = len(haystack) - 1

        i = 0
        j = 0
        index = 0

        while i <= x and j <= y:
            if needle[i] == haystack[j]:
                if i == x:
                    return index
                i += 1
                j += 1
            else:
                i = 0
                index += 1
                j = index
                
        return index - 1
            
                
                

        
