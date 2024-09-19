# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def mergeTwoLists(self, list1, list2):
        if list1 == None:
            return list2
        if list2 == None:
            return list1
        dummy = list1
        dummy2 = list2
        result = ListNode(None, None)
        dummyresult = result
        while True:

            if (dummy == None and dummy2 == None):
                break           
            elif (dummy != None and dummy2 == None):
                dummyresult.next = dummy
                dummyresult = dummyresult.next
                dummy = dummy.next
            elif (dummy == None and dummy2 != None):
                dummyresult.next = dummy2
                dummyresult = dummyresult.next
                dummy2 = dummy2.next
            else:
                if dummy.val < dummy2.val:
                        dummyresult.next = dummy
                        dummyresult = dummyresult.next
                        dummy = dummy.next
                else:
                    dummyresult.next = dummy2
                    dummyresult = dummyresult.next
                    dummy2 = dummy2.next
                    
        result = result.next
        return result
