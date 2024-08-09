class Solution(object):
    def rotate(self, nums, k):
        l = len(nums)
        
        if l <= 1 or k == 0:
            return nums
        if k > l:
            k = k % l

        nums[:] = nums[-k:] + nums[:l-k]

        return nums

        
