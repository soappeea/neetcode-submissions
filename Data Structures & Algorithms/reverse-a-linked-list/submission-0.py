# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # prev = previous node (starts as None, which will become the new tail)
        # curr = current node we're reversing
        prev, curr = None, head

        while curr:
            # Save the next node before changing the pointer
            temp = curr.next

            # Reverse current node's pointer to point backward
            curr.next = prev

            # Move prev forward to the current node
            prev = curr

            # Move curr to the next original node
            curr = temp

        # prev is now the new head of the reversed list
        return prev