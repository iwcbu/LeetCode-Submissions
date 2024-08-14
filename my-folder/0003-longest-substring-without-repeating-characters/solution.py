class Solution(object):
    def lengthOfLongestSubstring(self, s): 
        d = {}
        l = 0
        length = 0
        for i in range(len(s)):
            letter = s[i]
            
            if letter in d and d[letter] >= l:
                l = d[letter] + 1
            else:
                length = max(length, i - l + 1)
            d[letter] = i

        return length
