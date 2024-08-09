class Solution(object):
    def removeDuplicates(self, nums):

        x = 2
        
        for i in range(2, len(nums)):
            if nums[i] != nums[x-2]:
                nums[x] = nums[i]
                x += 1
        
        return x

