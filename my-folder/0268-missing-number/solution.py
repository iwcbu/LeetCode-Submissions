class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        expected = 0
        real = 0
        for i in range(len(nums)):
            expected += i + 1
            real += nums[i]

        return expected - real
        
