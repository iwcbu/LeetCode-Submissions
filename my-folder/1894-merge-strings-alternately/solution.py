class Solution(object):
    def mergeAlternately(self, word1, word2):

        i = 0
        a = []
        while i < len(word1) or i < len(word2):
            if i < len(word1):
                a.append(word1[i]) 
            if i < len(word2):
                a.append(word2[i])
            i += 1
        return ''.join(a)
