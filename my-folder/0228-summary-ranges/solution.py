class Solution(object):
    def summaryRanges(self, nums):
        """
        :type nums: List[int]
        :rtype: List[str]
        """
        result = []
        if len(nums) < 1:
            return []
        if len(nums) == 1:
            return [str(nums[0])]

        
        temp = []
        result= []

        for i in range(1, len(nums)):
            temp += [str(nums[i-1])]
            if nums[i] != nums[i-1] + 1 :
                if len(temp) < 2:
                    result += [temp[0]]
                else:
                    result += [temp[0] + "->" + temp[-1]]
                temp = []
            if i == len(nums) - 1:
                if nums[i] == nums[i-1] + 1 :
                    result += [temp[0] + "->" + str(nums[i])]
                else:
                    if len(temp) == 1:
                        result += [temp[0]]
                    elif len(temp) > 1:
                        result += [temp[0] + "->" + temp[-1]]

                    result += [str(nums[i])]

        return result
                
            
        
