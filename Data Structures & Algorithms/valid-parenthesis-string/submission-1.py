class Solution:
    def checkValidString(self, s: str) -> bool:

        # Brute force - Recursion - 3 possible.
        # f(ind) -> indicates possible valid string from 0 to i

        n = len(s)

        def f(ind, bal):
            if bal < 0 :
                return False
            if ind == n:
                return bal == 0
            if dp[ind][bal] != -1:
                return dp[ind][bal]
            
            if s[ind] == "(":
                dp[ind][bal] = f(ind+1,bal+1)
            elif s[ind] == ")":
                dp[ind][bal] = f(ind+1, bal-1)
            else:
                dp[ind][bal] = f(ind+1,bal+1) or f(ind+1, bal) or f(ind+1,bal-1)
            
            return dp[ind][bal]
        
        # ind: 0 - n, bal: 0 to n
        dp = [[-1 for _ in range(n)] for _ in range(n)]
        return f(0,0)