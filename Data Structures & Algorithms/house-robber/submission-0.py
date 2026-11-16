class Solution:
    def rob(self, nums: List[int]) -> int:
        # # Recursion
        # # f(n) = max(a[n] + f(n-2), f(n-1))

        # def dfs(ind):
        #     if ind < 0:
        #         return 0
        #     if ind == 0:
        #         return nums[ind]
        #     if dp[ind] != -1:
        #         return dp[ind]
            
        #     left = nums[ind] + dfs(ind-2)
        #     right = 0 + dfs(ind-1)

        #     dp[ind] = max(left, right)

        #     return dp[ind]

        n = len(nums)
        # dp = [-1 for _ in range(n)]
        # dfs(n-1)
        # return dp[n-1]


        prev = nums[0]
        prev_2 = 0

        for i in range(1, n):
            left = nums[i] + prev_2
            right = 0 + prev
            curr_i = max(left, right)

            prev_2 = prev
            prev = curr_i

        return prev

