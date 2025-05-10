class Solution(object):
    def minSum(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: int
        """
        i = len(nums1) - 1
        j = len(nums2) - 1
        sum1 = 0
        zeros1 = 0
        sum2 = 0
        zeros2 = 0

        while i >= -1 and j >= -1:
            if i == -1 and j == -1:
                break
            if i >= 0:
                if nums1[i] == 0:
                    zeros1 += 1
                    sum1 += 1
                    i -= 1
                else:   
                    sum1 += nums1[i]
                    i -= 1

            if j >= 0:
                if nums2[j] == 0:
                    zeros2 += 1
                    sum2 += 1
                    j -= 1
                else:
                    sum2 += nums2[j]
                    j -= 1
            
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


