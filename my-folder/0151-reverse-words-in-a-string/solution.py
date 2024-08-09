class Solution(object):
    def reverseWords(self, s):

        words = s.split()
        result = " ".join(words[::-1])

        return result

            



        
