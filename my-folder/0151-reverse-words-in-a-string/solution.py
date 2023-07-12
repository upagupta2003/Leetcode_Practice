class Solution:
    def reverseWords(self, s: str) -> str:
        s = re.sub('\s+', ' ', s).strip()
        ls = s.split(' ')
        s = " ".join(ls[::-1])
        return s


