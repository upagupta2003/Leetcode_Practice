class Solution:
    def isValid(self, s: str) -> bool:
        p_map = {"[":"]", "(":")", "{":"}"}
        stack = []

        for char in s:
            if char in p_map:
                stack.append(char)
            elif len(stack) == 0 or char != p_map[stack.pop()]:
                return False

        return len(stack) == 0
