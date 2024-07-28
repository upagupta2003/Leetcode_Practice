class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        n = int(sqrt(c)) + 1
        for a in range(n):
            b = sqrt(c - a*a)
            if b == int(b):
                return True
        return False

