class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = 0
        r = 0
        n = len(s)
        res = 0
        count = dict()

        for r in range(n):
            count[s[r]] = count.get(s[r], 0) + 1

            # Invalidity:
            if len(count) < (r - l + 1):
                count[s[l]] -= 1
                if count[s[l]] == 0:
                    count.pop(s[l])
                l += 1
            
            # Valid and update:
            if len(count) == (r - l + 1):
                res = max(res, r - l + 1)
        return res


#   zxyzyxz
#   l=1,r=4, 
#   res = 3
#   count = {z:1, x:1, y:2}
#
#