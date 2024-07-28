class Solution:

    def findMaxAverage(self, nums: List[int], k: int) -> float:
        if k == len(nums):
            return sum(nums)/k
        s = sum(nums[:k])
        ms = s
        for i in range(k,len(nums)):
            s = s  - nums[i-k] + nums[i]
            ms = max(ms,s)
        return ms/k
            
