# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or head.next==None:
            return head
        tortoise=head
        hare=head
        while hare!=None and hare.next!=None:
            hare=hare.next.next
            tortoise=tortoise.next
        return tortoise