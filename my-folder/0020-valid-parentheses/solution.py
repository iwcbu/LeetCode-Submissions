class Solution(object):
    def isValid(self, s):
        valid = 0
        
        bucket = "x"
        for x in s:
            if x == ")":
                if bucket[-1] != "(":
                    return False
                valid +=1
            if x == "]":
                if bucket[-1] != "[":
                    return False
                valid +=1
            if x == "}":
                if bucket[-1] != "{":
                    return False
                valid += 1
            
            bucket += x
            if valid == 1:
                valid = 0
                bucket = bucket[:-2]

        if bucket[-1] in "{[(":
            return False
                    
        return True
                
        
