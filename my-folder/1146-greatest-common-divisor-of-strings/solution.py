class Solution(object):
    def gcdOfStrings(self, str1, str2):
        if len(str1) == 0 or len(str2) == 0:
            return ""
        if set(str1) != set(str2):
            return ""
        if str1 == str2:
            return str1

        result_max = [x for x in range(1, len(str1)+1) if len(str1) % x== 0 and len(str2) % x == 0][-1]
        
        x = ""
        result = ""
        i = 0
        while i < len(str1) and i < len(str2):
            if (str1[i] == str2[i] and len(x) < result_max):
                x += str1[i]
                
            elif (str1[i] == str2[i] and len(x) >= result_max):
                result = x
                x = str1[i]
            else:
                x = ""
            i += 1

        if len(x) > len(result):
                result = x
        big_set = max([len(str1), str1], [len(str2), str2])[1]
        s1, s2 = set(result), set(max([len(str1), str1], [len(str2), str2])[1])
        if s1 != s2:
            return ""
        if result != x:
            return ""
        math = len(big_set) / result_max
        if result * math != big_set:
            return ""
        return result


            
