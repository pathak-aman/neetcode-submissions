# O(n2) - Generate all possible subarrays and find the maximum
# O(n) - Kadane's Algorithm

# [2,-3,4,-2,2,1,-1,4]
# i = 7
# curr_sum = 9
# max_sum = 9


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        curr_sum = 0
        max_sum = -float('inf')
        n = len(nums)

        for i in range(n):
            curr_sum += nums[i]
            max_sum = max(max_sum, curr_sum)
            if curr_sum < 0:
                curr_sum = 0
        return max_sum       
        