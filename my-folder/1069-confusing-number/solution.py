class Solution:
    def confusingNumber(self, n: int) -> bool:
        # Dict of confusing digts
        conf_dig = {0:0, 1:1, 6:9, 8:8, 9:6}
        orig = n
        rot = 0
        
        while n > 0:
            dig = n % 10
            n = n // 10
            
            if dig not in conf_dig:
                return False
            
            rot = rot  * 10 + conf_dig[dig]
        
        return rot != orig
                
        
        
        
        
