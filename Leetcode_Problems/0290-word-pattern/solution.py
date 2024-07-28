class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        map_index = {}
        word = s.split()

        if len(pattern) != len(word):
            return False
        for i in range(len(word)):
            c = pattern[i]
            w = word[i]

            char_key = 'char_{}'.format(c)
            char_w = 'word_{}'.format(w)

            if char_key not in map_index:
                map_index[char_key] = i 
            if char_w not in map_index:
                map_index[char_w] = i 
            if map_index[char_key] != map_index[char_w]:
                return False
        return True

