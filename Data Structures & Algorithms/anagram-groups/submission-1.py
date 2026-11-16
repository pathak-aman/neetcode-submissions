from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # For every string i compare with j
        # Compute frequency and compare and agregate.
        # Redoing Compute frequency -> Wasted

        # compute frequency once for all using array of 26 chars

        anagram_dict = defaultdict(list)

        for string in strs:
            char_arr = [0 for i in range(26)]
            for ch in string:
                char_arr[ord(ch) - ord('a')] += 1
            anagram_dict[tuple(char_arr)].append(string)
        return list(anagram_dict.values())

        



