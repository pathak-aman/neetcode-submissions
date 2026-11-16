class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        def get_code(word):
            count = [0]*26
            for char in word:
                count[ord(char) - ord('a')] +=1
            return count

        result = defaultdict(list)
        for word in strs:
            code = get_code(word)
            result[tuple(code)].append(word)
            # print(result.values())
        return result.values()
