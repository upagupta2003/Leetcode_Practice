# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head == None: return None
        odd = head
        even = head.next
        evenhd= even
        while (even!=None and even.next != None):
           odd.next = even.next
           odd=odd.next
           even.next = odd.next
           even=even.next
        odd.next = evenhd
        return head
    

