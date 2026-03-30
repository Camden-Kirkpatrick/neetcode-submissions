# Definition for singly-linked list.
class ListListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:

        if not list1 and not list2:
            return
        if not list1:
            return list2
        if not list2:
            return list1

        cur1 = list1
        cur2 = list2
        list3 = None

        if cur1.val < cur2.val:
                list3 = ListNode(cur1.val)
                cur1 = cur1.next
        else:
            list3 = ListNode(cur2.val)
            cur2 = cur2.next

        new_head = list3

        while cur1 and cur2:
            if cur1.val < cur2.val:
                list3.next = ListNode(cur1.val)
                list3 = list3.next
                cur1 = cur1.next
            else:
                list3.next = ListNode(cur2.val)
                list3 = list3.next
                cur2 = cur2.next

        while cur1:
            list3.next = ListNode(cur1.val)
            list3 = list3.next
            cur1 = cur1.next

        while cur2:
            list3.next = ListNode(cur2.val)
            list3 = list3.next
            cur2 = cur2.next
            

        return new_head
        