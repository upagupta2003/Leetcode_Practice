class Solution:
    def shortestWay(self, source: str, target: str) -> int:
        for i in target:
            if i not in source:
                return -1
        
        i,j = 0,0
        count = 0
        while j < len(target):
            if i == len(source):
                count = count + 1
                i = 0
            if source[i] == target[j]:
                j=j+1
            
            i=i+1
        return count + 1
                    
        
