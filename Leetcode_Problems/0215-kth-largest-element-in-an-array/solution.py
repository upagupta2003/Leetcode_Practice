import heapq
from typing import List

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
            heap = nums[:k]  
            heapq.heapify(heap)  # transforms list into a heap, in-place, in linear time
            for num in nums[k:]:
                if num > heap[0]:
                    heapq.heapreplace(heap, num)
            return heap[0]
