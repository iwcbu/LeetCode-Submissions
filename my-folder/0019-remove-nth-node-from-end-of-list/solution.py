# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: Optional[ListNode]
        :type n: int
        :rtype: Optional[ListNode]
        """

        prev = head
        cur = head.next
        nodes = []
        nodes.append([None, cur]) # prev, next

        while cur:
            nodes.append([prev, cur.next])
            prev = cur
            cur = cur.next
        
        remove = nodes[-n]
        if remove[0]:
            remove[0].next = remove[1]
        else:
            return remove[1]

        return head
        
        
