class Solution(object):
    def calPoints(self, operations):
        """
        :type operations: List[str]
        :rtype: int
        """

        result = []
        for x in operations:
            if x == "C":
                result.pop()
            elif x == "D":
                result.append(result[-1] * 2)
            elif x == "+":
                result.append(result[-1] + result[-2])
            else:
                result.append(int(x))

        return sum(result)


        
