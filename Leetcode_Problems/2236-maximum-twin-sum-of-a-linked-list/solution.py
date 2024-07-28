# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        temp = []
        node = head
        while node != None:
            temp.append(node.val)
            node = node.next
        i = 0
        j=len(temp)-1
        sm = 0
        while i < j:
            tmp_sm = temp[i] + temp[j]
            sm = max(sm,tmp_sm)
            i=i+1
            j=j-1
        return sm 
