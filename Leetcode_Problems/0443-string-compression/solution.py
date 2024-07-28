class Solution:
    def compress(self, chars: List[str]) -> int:
        curr_char = chars[0] # curr-char =  a
        ct = 0 
        for i in range(len(chars)):
            if curr_char == chars[0]:  # True 
                ct = ct+1              # ct = 1
                # chars.remove(chars[0]) # chars bbccc
            else:               
                # chars.remove(curr_char)      ## False, True curr_char = a , ct = 1
                chars.append(curr_char)      ## chars = bccca
                if ct != 1:
                    chars.extend(list(str(ct)))
                curr_char = chars[0]         ##curr_char = b
                ct = 1
            chars.pop(0)
        chars.append(curr_char)      ## chars = bccca
        if ct != 1:
            chars.extend(list(str(ct)))
        print(chars)
        return len(chars)

