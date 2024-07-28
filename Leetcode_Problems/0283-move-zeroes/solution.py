class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        """
        1. We use i to keep track of position of the first zero in the list (which changes as we go).
        2. We usejto keep track of the first non-zero value after the first zero (which is pointed by i).
        3. Each time we have i correctly points to a zero and j correctly points to the first non-zero after i, we swap the values that store at i and j.
        4. By doing this, we move zeros towards the end of the list gradually until j reaches the end.
        """

        l1 = len(nums)
        i=0
        for j in range(l1):
            if (nums[j] != 0):
                nums[i],nums[j] = nums[j], nums[i]
                i += 1
