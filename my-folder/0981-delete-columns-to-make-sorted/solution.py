class Solution(object):
    def minDeletionSize(self, strs):
        """
        :type strs: List[str]
        :rtype: int
        """
        delete = 0

        for col in range(len(strs[0])):

            lastChar = ord(strs[0][col])
            delThis = False

            for row in range(len(strs)):
                if delThis == True:
                    continue

                if row == 0:
                    continue

                if lastChar > ord(strs[row][col]):
                    delete += 1
                    delThis = True

                lastChar = ord(strs[row][col])
            
        
        return delete
                    
                

