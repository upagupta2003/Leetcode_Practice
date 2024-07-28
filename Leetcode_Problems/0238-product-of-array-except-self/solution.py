class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res =[]
        prod = math.prod(nums)
        for i in range(len(nums)):
            if nums[i] == 0:
                print("i=",nums[i])
                print("left prod=", math.prod(nums[:i]))
                print("rt prod=", math.prod(nums[i+1:]))
                prd = math.prod(nums[:i])*math.prod(nums[i+1:])
            else:
                prd = prod/nums[i]
            res.append(int(prd))
        return res


# class Solution:
#     def productExceptSelf(self, nums: List[int]) -> List[int]:
#         res =[]
#         prod = math.prod(nums)
#         for i in range(len(nums)):
#             prd = math.prod(nums[:i])*math.prod(nums[i+1:])
#             res.append(int(prd))
#         return res
