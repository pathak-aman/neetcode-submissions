class Solution:
    def lengthOfLongestSubstringKDistinct(self, s: str, k: int) -> int:
        # Brute
        # Generate all possible substrings
        # Compute char frequency 
        # If len of dict <= k, store the len of substring
        # Else break

        # TC - O(n2), SC - O(n)

        # Better - Two pointer & sliding window
        n = len(s)
        l = 0
        r = 0
        char_freq = {}
        ans = 0

        for r in range(n):
            char_freq[s[r]] = char_freq.get(s[r], 0) + 1

            # Invalid:
            if len(char_freq) > k:
                char_freq[s[l]] -= 1
                if char_freq[s[l]] == 0:
                    char_freq.pop(s[l])
                l += 1


            # Valid:
            if len(char_freq) <= k:
                ans = max(ans, r - l + 1)
        
        return ans

        # aabbecc k = 3
        # l = 4, r = 6, {e:1, c:2}; 3 > 2, ans = 5
        # TC: O(n + n) = O(2n), SC -> O(n)


