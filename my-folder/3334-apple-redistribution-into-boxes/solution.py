class Solution(object):
    def minimumBoxes(self, apple, capacity):
        """
        :type apple: List[int]
        :type capacity: List[int]
        :rtype: int
        """
        total = sum(apple)

        capSorted = sorted(capacity)
        capSorted = capSorted[::-1]
        num = 0
        for cap in capSorted:
            num += 1
            total = total - cap
            if total <= 0:
                break
        
        return num
        

