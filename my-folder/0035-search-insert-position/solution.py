class Solution(object):
    def searchInsert(self, nums, target):
        if target not in nums:
            if target < nums[0]:
                return 0
            if target > nums[-1]:
                return len(nums)
        for i in range(len(nums)):
            if nums[i] == target or target < nums[i]:
                return i
