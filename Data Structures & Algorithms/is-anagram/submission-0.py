class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # if len mistahc return False
        # O(nlogn) - Sort and compare
        # O(n)

        if len(s) != len(t):
            return False
        
        s_char_map = {}
        t_char_map = {}
        for char_s, char_t in zip(s,t):
           s_char_map[char_s] = s_char_map.get(char_s,0) + 1
           t_char_map[char_t] = t_char_map.get(char_t,0) + 1

        return s_char_map == t_char_map
