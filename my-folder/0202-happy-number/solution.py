class Solution(object):
    def isHappy(self, n):

        inv = set()

        while n not in inv:
            inv.add(n)
            digits_list = list(str(n))
            num_sum = 0

            for digit in digits_list:
                num_sum += int(digit) ** 2
            n = num_sum
            
            if n == 1:
                return True

        return False


        

        

        
