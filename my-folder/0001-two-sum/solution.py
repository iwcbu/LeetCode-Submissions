class Solution(object):
    def twoSum(self, nums, target):
        hashmap = {}

        for i in range(len(nums)):
            p = target - nums[i]
            if p in hashmap:
                return [hashmap[p], i]
                
            hashmap[nums[i]] = i


        
