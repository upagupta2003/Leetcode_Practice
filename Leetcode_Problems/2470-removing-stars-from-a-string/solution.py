class Solution:
    def removeStars(self, s: str) -> str:
        s_list = []
        for i in range(len(s)):
            if s[i].isalpha():
                s_list.append(s[i])
            elif s[i] == "*":
                s_list.pop()
        
        return ''.join(s_list)

        
