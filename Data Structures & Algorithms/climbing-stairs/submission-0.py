class Solution:
    def climbStairs(self, n: int) -> int:
        dp = [-1 for _ in range(n+1)]
        # Count all possible of something -> Recursion
        # Top to bottom approach:
        # f(0) -> No of ways to reach the top stair = 1, returning a 0 means there's no possible way, which is wrong. 

        # f(n) = f(n-1) + f(n-2)
        def f(n, dp):
            # Base case:
            if n < 0:     # Invalid height 
                return 0
            if n == 0:
                return 1

            if dp[n] != -1:
                return dp[n]
            
            left = f(n-1, dp)
            right = f(n-2, dp)

            sum = left + right
            dp[n] = sum
            return sum
        f(n, dp)
        return dp[n]

