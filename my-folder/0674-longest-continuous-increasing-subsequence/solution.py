class Solution(object):
    def findLengthOfLCIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        if n < 2:
            return n

        left, right = 0, 1
        result = 1
        while right < n and left <= right:
            if nums[right] > nums[right-1]:
                right += 1
            else:
                if (right-left) > result:
                    result = right-left
                left = right
                right += 1
        
        return max(result, (right-left))
                

        
