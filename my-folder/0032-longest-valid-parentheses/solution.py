class Solution(object):
    def longestValidParentheses(self, s):
        """
        :type s: str
        :rtype: int
        """
        if len(s) <= 1:
            return 0

        pQ = []
        arr = [0] * len(s)

        #convert parentheses pairings into a 01 array
        for i in range(len(s)):
            if s[i] == "(":
                pQ.append(i)

            if s[i] == ")" and len(pQ) > 0:
                a = pQ.pop()
                arr[a] = 1
                arr[i] = 1

        #find longest number of consecutive 1s
        best, curr = 0, 0
        for num in arr:
            if num == 1:
                curr += 1
            else:
                best = max(curr, best)
                curr = 0
        
        return max(best, curr)
        
        

        
        
            

            
            
            

        
