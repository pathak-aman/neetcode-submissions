class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # O(n2) - Every pairs
        # O(nlogn) - sort and two pointers
        # O(N), O(N) - using hashmap

        nums_index_dict = {}
        n = len(nums)

        for i in range(n):
            diff = target - nums[i]
            if diff in nums_index_dict:
                return sorted([i,nums_index_dict[diff]])
            nums_index_dict[nums[i]] = i
