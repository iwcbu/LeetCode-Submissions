class Solution(object):
    def minSum(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: int
        """
        sum1 = sum(nums1)
        zeros1 = nums1.count(0)
        sum2 = sum(nums2)
        zeros2 = nums2.count(0)

        if zeros1 > 0:
            sum1 += zeros1
        if zeros2 > 0:
            sum2 += zeros2
            
        if sum1 == sum2:
            return sum1
        if sum1 > sum2:
            if zeros2 > 0:
                return sum1
            else:
                return -1
        if sum1 < sum2:
            if zeros1 > 0:
                return sum2
            else:
                return -1


