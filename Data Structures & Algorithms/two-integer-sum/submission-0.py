class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        pos_dict = dict()
        for start, num in enumerate(nums):
            if num in pos_dict:
                return [pos_dict[num], start]
            else:
                pos_dict[target-num] = start