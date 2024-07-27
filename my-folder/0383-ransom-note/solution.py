from collections import Counter
class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        rn = Counter(ransomNote)
        mag = Counter(magazine)

        for char,count in rn.items():
            if mag[char] < count:
                return False
        return True

