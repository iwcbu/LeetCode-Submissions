class Solution(object):
    def myAtoi(self, s):
        """
        :type s: str
        :rtype: int
        """
        string = s.strip()
        ubound = "2147483647"
        lbound = "-2147483648"
        str123 = "1234567890"
        
        #helper function
        def isInBound(defString):
            #for negative sign
            if defString[0] == "-":
                defString2 = defString
                if len(defString2) < len(lbound):
                    return int(defString)
                if len(defString2) > len(lbound):
                    count = 1
                    defString2 = "-"
                    while count < len(defString):
                        if defString[count] != "0":
                            defString2 += defString[count:]
                            break
                        count += 1
                    if defString2 == "-":
                        return 0
                if len(defString2) > len(lbound):
                    return int(lbound)
                if len(defString2) < len(lbound):
                    return int(defString2)
                sol = "-"
                for i in range(1, len(defString2)):
                    if int(defString2[i]) > int(lbound[i]):
                        return int(lbound)
                    if int(defString2[i]) < int(lbound[i]):
                        return int(defString2)

                    sol += defString2[i]
                return int(sol)
            
            #For positive sign
            if defString[0] == "+":
                defString2 = defString
                if len(defString2) < len(lbound):
                    return int(defString)
                if len(defString2) > len(lbound):
                    count = 1
                    defString2 = ""
                    while count < len(defString):
                        if defString[count] != "0":
                            defString2 += defString[count:]
                            break
                        count += 1
                    if defString2 == "":
                        return 0
                
                if len(defString2) < len(ubound):
                    return int(defString2)
                if len(defString2) > len(ubound):
                    return int(ubound)    
                sol = ""
                for i in range(len(defString2)):
                    if int(defString2[i]) > int(ubound[i]):
                        return int(lbound)
                    if int(defString2[i]) < int(ubound[i]):
                        return int(defString2)

                    sol += defString2[i]
                return int(sol)

            #for numbers without a sign
            else:
                defString2 = defString
                if len(defString2) < len(ubound):
                    return int(defString)
                if len(defString2) > len(ubound):
                    count = 0
                    defString2 = ""
                    while count < len(defString):
                        if defString[count] != "0":
                            defString2 += defString[count:]
                            break
                        count += 1
                    if defString2 == "":
                        return 0
                if len(defString2) > len(ubound):
                    return int(ubound)
                if len(defString2) < len(ubound):
                    return int(defString2)
                sol = ""
                for i in range(len(defString)):
                    if int(defString[i]) > int(ubound[i]):
                        return int(ubound)
                    if int(defString2[i]) < int(ubound[i]):
                        return int(defString2)

                    sol += defString[i]
                return int(sol)
        #end of helper

        #start of code
        if len(string) <= 1:
            if string == "":
                return 0
            if string in str123:
                return int(string)
            return 0

        elif string[0] == "-":
            result = "-"
            for i in range(1, len(string)):
                if string[i] not in str123:
                    if result == "-":
                        return 0
                    return isInBound(result)
                result += string[i]
            return isInBound(result)
        
        elif string[0] == "+":
            result = ""
            for i in range(1, len(string)):
                if string[i] not in str123:
                    if result == "":
                        return 0
                    return isInBound(result)
                result += string[i]
            return isInBound(result)
        


        elif string[0] in str123:
            result = ""
            for i in range(len(string)):
                if string[i] not in str123:
                    if result == "":
                        return 0
                    return isInBound(result)
                result += string[i]
            return isInBound(result)
                
        elif string[0] not in str123:
            return 0


            
                

                    
