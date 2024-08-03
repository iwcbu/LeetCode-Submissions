class Solution(object):
    def isPalindrome(self, x):
        str_x = str(x)
        half_x = len(str_x) / 2
        for i in range(half_x):
            j = i + 1
            if str_x[i] != str_x[-j]:
                return False

        return True


