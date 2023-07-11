class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        # for i in range(len(nums)-2):
        #     if nums[i]<nums[i+1] and nums[i+1]<nums[i+2]:
        #         return True
        # return False

        if len(nums) < 3:
            return False

        first = second = math.inf

        for num in nums:
            if num <= first:
                first = num
            elif num <= second:
                second = num
            else:
                return True

        return False
