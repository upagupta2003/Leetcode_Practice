class Solution:
    
    def validateIpv4(self, ip: str) -> str:
        ipList = ip.split(".")

        if len(ipList) != 4:
            return "Neither"

        for i in ipList:
            if not i.isnumeric():
                return "Neither"
            if len(i) >=2 and i[0] == '0':
                return "Neither"
            
            if not (0<= int(i) <= 255):
                return "Neither"
        return "IPv4"


    def validateIpv6(self, ip: str):
        nums = ip.split(':')
        hexdigits = '0123456789abcdefABCDEF'
        for x in nums:
            # Validate hexadecimal in range (0, 2**16):
            # 1. at least one and not more than 4 hexdigits in one chunk
            # 2. only hexdigits are allowed: 0-9, a-f, A-F
            if len(x) == 0 or len(x) > 4 or not all(c in hexdigits for c in x):
                return "Neither"
        return "IPv6"
    
    def validIPAddress(self, queryIP: str) -> str:
        if queryIP.count('.') == 3:
            return self.validateIpv4(queryIP)

        elif queryIP.count(':') == 7:
            return self.validateIpv6(queryIP)
        else:
            return "Neither"


