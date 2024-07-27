class Solution:
    def isPalindrome(self, s: str) -> bool:
        if s == "":
            return True
        filterd_s = []
        s = s.lower().replace(" ", "")
        for ch in s:
            if ch.isalnum():
                filterd_s.append(ch)
        return filterd_s == filterd_s[::-1]
          
