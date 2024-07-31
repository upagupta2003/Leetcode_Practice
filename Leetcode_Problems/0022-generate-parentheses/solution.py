class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []

        def check_paranthesis(left,right,stack,cand):
            if left == right == 0:
                res.append(cand)
                return
            if left > 0:
                check_paranthesis(left-1,right,stack+1,cand+"(")
            if right > 0 and stack > 0:
                check_paranthesis(left, right-1, stack-1, cand+")")
        check_paranthesis(n, n, 0, "")
        return res

