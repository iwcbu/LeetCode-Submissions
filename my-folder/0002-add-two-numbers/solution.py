# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        l1_index = l1
        l2_index = l2
        result = 0
        count = 0
        while l1_index is not None or l2_index is not None:
            if l1_index is not None:
                result += l1_index.val * (10 ** count)
                l1_index = l1_index.next
            if l2_index is not None:
                result += l2_index.val * (10 ** count)
                l2_index = l2_index.next
            count += 1
        
        string = str(result)[::-1]
        l3 = ListNode(string[0])
        if len(string) == 1:
            return l3
        current_node = l3
        for i in range(1, len(string)):
            new_node = ListNode(string[i])
            current_node.next = new_node
            current_node = new_node

        return l3

            



