class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        # Count all possible path -> Recursion
        # f(i,j) -> Counts all possible path from 0,0 to i,j
        # f(m-1, n-1)

        def paths(i,j):
            # Base case
            if i == 0 and j == 0:
                return 1
            if i < 0 or j < 0 :
                return 0
            if dp[i][j] != -1:
                return dp[i][j]
            
            up = paths(i-1,j)
            left = paths(i, j-1)

            dp[i][j] = up + left

            return dp[i][j] 

        dp = [[-1 for _ in range(n)] for _ in range(m)]
        return paths(m-1, n-1)
        