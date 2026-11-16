class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        l = 0
        r = 1
        max_profit = 0
        curr_profit = 0

        while r < n:
            if prices[l] <= prices[r]:
                curr_profit = prices[r] - prices[l]
                max_profit = max(max_profit, curr_profit)
            else:
                # New local minima
                l = r
            r += 1
        return max_profit
        
        # max_profit = max(max_profit, curr_profit)


# # [1,2,3,0]
# l = 3
# r = 4
# maxp = 7