class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        mc = max(candies)
        ls = []
        for i in range(len(candies)):
            current_candies = extraCandies + candies[i]
            if (current_candies >= mc):
                ls.append(True)
            else:
                ls.append(False)      
        return ls
            
