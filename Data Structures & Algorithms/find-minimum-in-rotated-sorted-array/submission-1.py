class Solution:
    def findMin(self, nums: List[int]) -> int:
        # Minimum can be in any half. The sorted or the not sorted.
        # Safe bet: Identify the sorted
        # Store the minimum of the sorted half and eliminate it
        # And explore the unsorted half

        low = 0
        minimum = float("inf")
        minimum_pos = -1
        high = len(nums) - 1

        while low <= high:
            mid = (low + high) // 2

            # Left sorted
            if nums[low] <= nums[mid]:
                minimum = min(minimum, nums[low])
                # For index, keep track of minimum_pos
                low = mid + 1

            # Right sorted
            else:
                minimum = min(minimum, nums[mid])
                high = mid -1
        
        return minimum