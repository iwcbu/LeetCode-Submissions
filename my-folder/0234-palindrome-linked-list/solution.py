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
        

        arr = []
        cur = head
        
        while cur != None:
            arr.append(cur.val)
            cur = cur.next
        
        lenarr = len(arr)

        if lenarr <= 1:
            return True

        for i in range(lenarr):
            noti = (i+1) * -1
            if arr[i] != arr[noti]:
                return False

        return True

        


        
        
