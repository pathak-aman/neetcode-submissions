class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:

# 2,4,10, 1,5
# k=2:
# [2] [4,10,1,5] = 2, 20 -> 20
# [2,4] [10,1,5] = 6, 16 -> 16
# [2,4,10] [1,5] = 16,6 -> 16
# [2,4,10,1][5] = 17,5 -> 17

# 16
# [2,4,10][1,5]

# 10,11,12,....16,17,18,19
# x             V   V  V V
# low                    high

# First possible

# Pseudo code:
# Apply binary search on the range
# Find mid, see valid split is possible
# If yes, shift high to mid - 1
# Else shift low to mid + 1
# Repeat until low <= high

        low = -1
        high = 0

        for num in nums:
            low = max(low, num)
            high += num

        def canSplit(nums, k , sumarr):
            subarrays = 1
            curr_sum = 0
            for num in nums:
                curr_sum += num
                if curr_sum > sumarr:
                    subarrays += 1
                    curr_sum = num
            return subarrays <= k
    
        while low <= high:
            mid = (low + high) // 2
            if canSplit(nums, k, mid):
                ans = mid
                high = mid - 1
            else:
                low = mid + 1
        return low
