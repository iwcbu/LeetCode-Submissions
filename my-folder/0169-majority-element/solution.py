class Solution(object):
    def majorityElement(self, nums):
        
        dic = {}
        for x in nums:
            if x not in dic:
                dic[x] = 1
            else:
                dic[x] += 1
                
        key = max(dic.values())
        return [k for k, x in dic.items() if x == key][0]
        
