class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
       #comparing the concatenated Strings if they are equal or not
       #If thy are not we will return null
       # else find the highest common factor(hcf) and return the substring with length (o,hcf)
        if (str1 + str2 != str2 + str1):
           return ""
        else:
            hcf = gcd(len(str1),len(str2))
            return str1[0:hcf]


