class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()
        for i in range(len(nums)):
            if nums[i] > 0:
                break
            if i == 0 or nums[i - 1] != nums[i]:
                self.twosum2(nums, i, res)
        return res

    def twosum2(self, nums: [list], i: int, res: List[List[int]]):
        lo, hi = i + 1, len(nums) - 1
        while lo < hi:
            sum = nums[i] + nums[lo] + nums[hi]
            if sum < 0:
                lo = lo + 1
            elif sum > 0:
                hi = hi - 1
            else:
                res.append([nums[i], nums[lo], nums[hi]])
                lo = lo + 1
                hi = hi - 1
                while lo < hi and nums[lo] == nums[lo - 1]:
                    lo = lo + 1

