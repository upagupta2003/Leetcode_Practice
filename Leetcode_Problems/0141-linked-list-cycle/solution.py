# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        seen = set()
        current = head
        while current is not None:
            if current in seen:
                return True
            else:
                seen.add(current)
                current = current.next
        return False

        
