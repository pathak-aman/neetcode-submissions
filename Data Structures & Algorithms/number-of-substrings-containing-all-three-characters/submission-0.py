class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        
        l = 0
        r = 0
        n = len(s)
        res = 0
        count = dict()

        for r in range(n):
            count[s[r]] = count.get(s[r],0) + 1

            while len(count) == 3:
                res += n - r
                count[s[l]] -= 1
                if count[s[l]] == 0:
                    count.pop(s[l])
                l += 1
        return res


    # abacab.   # aabbcc.  # aaabc
    # a:1,b:1,c:1
    # l=3, r=5, res = 3 + 3 + 1 + 1

    # 2 + 2
    # 3


