class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        map_index = {}

        for i in range(len(nums)):
            if (target - nums[i]) not in map_index:
                map_index[nums[i]] = i 
            else:
                return [map_index.get(target-nums[i]),i]
        
