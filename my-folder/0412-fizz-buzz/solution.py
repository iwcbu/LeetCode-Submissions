class Solution(object):
    def fizzBuzz(self, n):
        """
        :type n: int
        :rtype: List[str]
        """

        answer = []
        for i in range(n+1):
            if i == 0:
                continue
            else:
                if i % 3 == 0 and i % 5 != 0:
                    answer += ["Fizz"]
                if i % 5 == 0 and i % 3 != 0:
                    answer += ["Buzz"]
                if i % 3 == 0 and i % 5 == 0:
                    answer += ["FizzBuzz"]
                if i % 3 != 0 and i % 5 != 0:
                    answer += [str(i)]

        return answer
        

        
        
