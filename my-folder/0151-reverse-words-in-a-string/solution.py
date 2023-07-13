class Solution:
    def reverseWords(self, s: str) -> str:
        temp = None
        res = []
        for i in s:
            if i != " ":
                if temp is None:
                    temp = i
                else:
                    temp=operator.concat(temp,i)   
            else:
                print(temp)
                if temp is not None:
                    res.insert(0,temp)
                temp = None
        if temp is not None:
            res.insert(0,temp)
        return " ".join(res) 
                
                    





