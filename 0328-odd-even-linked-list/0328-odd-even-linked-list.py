# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head

        odd = head
        even = head.next
        even_head = even

        while even and even.next:
            # Connect current odd node to next odd node
            odd.next = even.next
            odd = odd.next

            # Connect current even node to next even node
            even.next = odd.next
            even = even.next

        # Attach even list after odd list
        odd.next = even_head

        return head
        