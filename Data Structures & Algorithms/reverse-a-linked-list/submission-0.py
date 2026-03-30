# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = None
        curr = head
        while curr is not None:
            # Store the next node so we don't lose access to the rest of the list
            nxt = curr.next
            # Point to the previous node instead of the next node
            # The first node will point to None, since it's now the tail node
            curr.next = prev
            # Update the previous node to be the current node
            prev = curr
            # Move to the next node
            curr = nxt

        return prev
        