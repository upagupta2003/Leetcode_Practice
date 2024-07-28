from collections import Counter


class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        count_s = Counter(s)
        print(count_s)

        for ch in t:
            count_s[ch] -= 1
        
        print(count_s)

        for val in count_s.values():
            if val != 0:
                return False

        return True

