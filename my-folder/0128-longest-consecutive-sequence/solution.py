class Solution(object):
    def longestConsecutive(self, nums):
        if len(nums) <= 0:
            return 0
        numset = set(nums)
        best = 0
        for num in numset:
            if num - 1 not in numset:
                current_num = num
                current_length = 1
                while current_num + 1 in numset:
                    current_num += 1
                    current_length += 1
                
                best = max(best, current_length)

        return best





                
             
        
