class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        count = 0
        for i in range(len(flowerbed)):
            if flowerbed[i] == 0:
                left_plot = True if (i == 0 or flowerbed[i-1] == 0) else False
                right_plot = True if (i == len(flowerbed)-1 or flowerbed[i+1] == 0) else False
                if left_plot and right_plot:
                    flowerbed[i] = 1
                    count = count + 1
            if count >= n:
                return True
        return False           
        
        


