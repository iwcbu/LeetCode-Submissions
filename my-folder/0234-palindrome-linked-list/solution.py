# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def isPalindrome(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: bool
        """

        if head.next == None:
            return True
        
    
        stack = []
        cur1 = head
        cur2 = head
        lenlist = 0

        while cur1 and cur2:
            stack.append(cur1.val)
            cur1 = cur1.next
            cur2 = cur2.next
            lenlist += 1
            if cur2 == None:
                break
            cur2 = cur2.next
            lenlist += 1
        
        lenstack = len(stack)
        if lenstack < 2:
            val = stack.pop()
            if cur1.val == val:
                return True
            else:
                return False

        if lenlist % 2 == 1:
            stack.pop()
        
        while cur1:
            val = stack.pop()
            if val != cur1.val:
                return False
            cur1 = cur1.next
        
        return True
        


        
        
