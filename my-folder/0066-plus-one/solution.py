class Solution(object):
    def plusOne(self, digits):
        if len(digits) == 0:
            return [1]
        if digits[-1] != 9:
            digits[-1] += 1
            return digits
        return self.plusOne(digits[:-1]) + [0]

        


        
        
        
