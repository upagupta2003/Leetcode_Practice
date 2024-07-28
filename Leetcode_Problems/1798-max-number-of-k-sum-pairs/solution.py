class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        # c = 0
        # for i in nums:
        #     if k-i in nums:
        #         c = c+1
        #         nums.remove(i)
        #         nums.remove(k-i)
        # return c

        c=0
        nums.sort()
        i=0
        j=len(nums)-1
        while i < j:
            if nums[i] + nums[j] < k:
                i = i+1
            elif nums[i] + nums[j] > k:
                j = j-1
            else:
                i=i+1
                j=j-1
                c = c+1
        return c
