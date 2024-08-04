class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: None Do not return anything, modify nums1 in-place instead.
        """
        if m + n == n:
            nums1[:] = nums2

        i1 = m - 1
        i2 = n - 1

        while i1 >= 0 and i2 >= 0:
            if nums1[i1] < nums2[i2]:
                nums1[:] = nums1[:i1 + 1] + [nums2[i2]] + nums1[i1 + 1:-1]
                i2 -= 1
            elif i1 == 0 and nums1[i1] >= nums2[i2]:
                nums1[:] = [nums2[i2]] + nums1[i1:-1]
                i2 -= 1
            else: 
                i1 -= 1
        
