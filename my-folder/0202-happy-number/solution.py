class Solution:
    def isHappy(self, n: int) -> bool:

        def digit_sqr(n: int) -> int:
            sqr_num = 0
            while n > 0:
                sqr_num = sqr_num + (n%10) ** 2
                n = n//10
            return sqr_num

        seen = set()

        while (n != 1) and (n not in seen):
            seen.add(n)
            n = digit_sqr(n)

        return n == 1    


        
