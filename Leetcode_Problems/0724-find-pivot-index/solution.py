class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        ls = 0
        rs = 0
        for i in range(len(nums)):
            ls = sum(nums[:i])
            rs = sum(nums[i+1:len(nums)])
            if rs == ls:
                return i

        return -1

        
