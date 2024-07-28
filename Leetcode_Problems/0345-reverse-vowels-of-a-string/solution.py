class Solution:
    
    def reverseVowels(self, s: str) -> str:
        i = 0;
        j = len(s)-1
        chars = list(s)
        vowels = ["a","e","i","o","u","A","E","I","O","U"]

        while(i < j):
            if chars[i] in vowels:
                if chars[j] in vowels:
                    temp = chars[i]
                    chars[i]= chars[j]
                    chars[j] = temp
                    j=j-1
                    i=i+1
                else:
                    j=j-1
            else:
                i=i+1
                     
                    
        return ''.join(chars)





