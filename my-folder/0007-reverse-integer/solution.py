class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        if x == 0:
            return 0
        
        
        string = str(x)
        arr = list(string)
        i = -1

        while True:
            if arr[i] != "0":
                break
            arr.pop()
        
        string = ''.join(arr)
        if x < 0:
            part = string[1:]
            res = string[0] + part[::-1]
        else:
            res = string[::-1]

        result = int(res) 

        if result > 2147483647 or result < -2147483648:
            return 0

        return result

        

            
        
