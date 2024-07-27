class Solution:
    def sortJumbled(self, mapping: List[int], nums: List[int]) -> List[int]:
        mapped_list = []

        for i in range(len(nums)):
            number = str(nums[i])
            formed = ""
            for j in range(len(number)):
                formed = formed + str(mapping[int(number[j])])
            mapped_list.append((int(formed),i))
        
        mapped_list.sort()
        answer = []
        for i in mapped_list:
            answer.append(nums[i[1]])
        

        print(answer)

        return answer







        
