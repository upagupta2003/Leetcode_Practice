class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        length = len(nums)
        L,R,ans = [0]*length,[0]*length,[0]*length
        L[0] = 1
        for i in range(1,length):
            L[i] = nums[i-1] * L[i-1]
        R[length - 1] = 1
        for i in reversed(range(length-1)):
            R[i] = nums[i+1] * R[i+1]
        for i in range(length):
            ans[i] = L[i] * R[i]
        return ans


# class Solution:
#     def productExceptSelf(self, nums: List[int]) -> List[int]:
#         res =[]
#         prod = math.prod(nums)
#         for i in range(len(nums)):
#             prd = math.prod(nums[:i])*math.prod(nums[i+1:])
#             res.append(int(prd))
#         return res
