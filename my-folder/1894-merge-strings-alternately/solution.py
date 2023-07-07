class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        l1 = len(word1)
        l2 = len(word2)
        res = ''
        if (l1 == l2):
            for i in range(l1):
                res = res + word1[i]
                res = res + word2[i]
        elif (l1 < l2):
            for i in range(l1):
                res = res + word1[i]
                res = res + word2[i]
            res = res + word2[i+1:l2]
        elif (l1 > l2):
            for i in range(l2):
                res = res + word1[i]
                res = res + word2[i]
            res = res + word1[i+1:l1]

            
        return res
        



