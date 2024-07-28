class Solution:
    def average(self, salary: List[int]) -> float:
#         sum = 0
#         count = 0
#         salary = sorted(salary)
#         for i in range(1,len(salary)-1):
#             sum = sum + salary[i]
#             count = count + 1
#         return sum/count
        a = min(salary)
        b = max(salary)
        total = sum(salary) - a - b
        return total/(len(salary)-2)
