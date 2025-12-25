class Solution(object):
    def findShortestSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        count = {}
        first = {}
        last = {}

        for i in range(len(nums)):
            n = nums[i]
            if n not in count:
                count[n] = 0
                first[n] = i
            last[n] = i
            count[n] += 1

        maxCount = max(count.values())
        result = len(nums)

        for term in count:
            if count[term] == maxCount:
                result = min(result, last[term] - first[term] + 1)
        
        return result
                


                

    

            


