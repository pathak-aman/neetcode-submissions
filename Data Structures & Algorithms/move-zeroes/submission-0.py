class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        r = 0
        n = len(nums)
        zero_pos = 0

        for i in range(n):
            if nums[i]:
                zero_pos += 1
            else:
                break

        
        for i in range(zero_pos+1, n):
            if nums[i]:
                nums[zero_pos], nums[i] = nums[i], nums[zero_pos]
                zero_pos += 1
        return nums


# [1,2,4,0,0,0,0,8]
# zero_pos = 3
# i = 4

# [1,2,5,0,0,0]
# zero_pos = 2
# i = 5




        