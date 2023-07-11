class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        num1 = set(nums1)
        num2 = set(nums2)
        result = [[],[]]
        for i in num2:
            if i not in num1:
                result[1].append(i)
                
        
        for i in num1:
            if i not in num2:
                result[0].append(i)
                

        return result

    

