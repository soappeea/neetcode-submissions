# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
            # list1 and list2 initially point to the heads of their linked lists

            # dummy stays at the beginning so we can return the merged list
            # node tracks the last node (tail) of the merged list
            dummy = node = ListNode()

            # Continue comparing while both lists have nodes remaining
            while list1 and list2:

                if list1.val < list2.val:
                    # Attach the smaller node from list1 to the merged list
                    node.next = list1

                    # Move list1 to its next node
                    list1 = list1.next
                else:
                    # Attach the smaller node from list2 to the merged list
                    node.next = list2

                    # Move list2 to its next node
                    list2 = list2.next

                # Move node to the node we just attached
                # node always points to the tail of the merged list
                node = node.next

            # One list is empty, so attach the remaining nodes from the other
            node.next = list1 or list2

            # Return the head of the merged list, skipping the dummy node
            return dummy.next
