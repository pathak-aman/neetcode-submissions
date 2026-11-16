class Solution:
    def climbStairs(self, n: int) -> int:
        # Count all possible of something -> Recursion
        # f(n) = f(n-1) + f(n-2)
        
        # dp = [-1 for _ in range(n)]
        # def dfs(ind, dp):
        #     # Base Case:
        #     if ind == n:
        #         return 1
        #     if ind > n:
        #         return 0
        #     if dp[ind] != -1:
        #         return dp[ind]

        #     dp[ind] = dfs(ind+1,dp) + dfs(ind+2, dp)
        #     return dp[ind]

        # return dfs(0,dp)



        # f(i) -> Represent the number of ways to climb stairs from i to 0.
        def f(ind):
            if ind == 0 or ind == 1:
                return 1
            if dp[ind] != -1:
                return dp[ind]

            one = f(ind-1)
            two = f(ind-2)
            dp[ind] = one + two
            return dp[ind]
        
        dp = [-1 for i in range(n+1)]
        f(n)
        return f(n)
            
