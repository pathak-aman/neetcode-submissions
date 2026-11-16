# O(n2) - Generate subarrays, compute the length by j-i+1.

# Sliding window fails - lacks monotonicity
# Binary Search fails as well
# Prefix sum appraoch:
# sum[i...j] = p[j+1] - p[i]
#   X-K     K 
# |----||------|
# |------------| sum = X
# K = X - p[i]
# p[i] = X - K
# O(n), O(n)



class Solution:
    def maxSubArrayLen(self, nums: List[int], k: int) -> int:
        n = len(nums)
        total = 0
        max_length = 0
        prefix_index = {0:-1}

        for i in range(n):
            total += nums[i]
            to_find = total - k
            if to_find in prefix_index:
                index = prefix_index[to_find]
                max_length = max(max_length, i - index)
            
            if not total in prefix_index:
                # Update only once for longest
                prefix_index[total] = i
        return max_length


# [1,2,-3,4,6,4,2]
# k=3
# {1:0, 3:1, 0:2}




