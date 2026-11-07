# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        slow, fast = head, head.next
        # split into 2 lists
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        # second is first elem of second half of list
        second = slow.next
        prev = slow.next = None # disconnect 2 lists
        # reverse the 2 lists
        while second:
            temp = second.next
            second.next = prev
            prev = second
            second = temp
        
        # merge 2 lists
        first, second = head, prev #[2, 4] and [8, 6] prev is 8
        while second:
            tmp1, tmp2 = first.next, second.next
            first.next = second
            second.next = tmp1
            first, second = tmp1, tmp2