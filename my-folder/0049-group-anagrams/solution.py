class Solution(object):
    def groupAnagrams(self, strs):

        group = {}
        for x in strs:
            x_sorted = ''.join(sorted(x))
            if x_sorted not in group:
                group[x_sorted] = [x]
            else:
                group[x_sorted] += [x]
        
        return list(group.values())

