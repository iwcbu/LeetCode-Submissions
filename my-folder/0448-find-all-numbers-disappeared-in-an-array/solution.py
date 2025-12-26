class Solution(object):
    def findDisappearedNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        n = len(nums)
        sn = set(nums)
        result = []

        for number in range(1, n+1):
            if number not in sn:
                result.append(number)

        return result




        
