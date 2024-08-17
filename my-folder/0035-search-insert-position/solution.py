class Solution(object):
    def searchInsert(self, nums, target):
        if len(nums) == 0:
            return 0
            
        if nums[0] == target:
            return 0
            
        if nums[0] < target:
            return 1 + self.searchInsert(nums[1:], target)
            
        if nums[0] > target:
            return 0
