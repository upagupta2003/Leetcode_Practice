class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        if s == t: ##if they are same return true
            return True
        else:
            ##converting strings to list so that i can have  have the positns of each charater 
            ls = list(s)
            lt = list(t)
            i,j = 0,0
            ## Now, here running the loop to check each character
            while i < len(ls) and j < len(lt):
                if ls[i] == lt[j]: ## to compare characers
                    i=i+1 ## if found increment the pointer by 1 in s
                j=j+1 ## increment in t
            return i == len(ls)

            

                

