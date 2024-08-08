class Solution:
    def decodeMessage(self, key: str, message: str) -> str:
        alp = "abcdefghijklmnopqrstuvwxyz"
        decoder = {}

        answer = ""
        index = 0
        for ch in key:
            if ch != " " and ch not in decoder:
                decoder[ch] = index
                index += 1
                #print(f"decoder: {decoder}")
        
        for ch in message:
            if  ch == " ":
                answer += " "
            else:
                answer += alp[decoder[ch]]

        return answer

