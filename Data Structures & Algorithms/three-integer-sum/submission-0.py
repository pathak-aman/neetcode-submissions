class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # Brute Force:
        # n = len(nums)
        # nums.sort()
        # result = set()
        # for i in range(n):
        #     for j in range(i+1, n):
        #         for k in range(j+1,n):
        #             if (nums[i]+nums[j]+nums[k] == 0 and 
        #             i != j and j !=k and i!= k):
        #                 result.add(tuple([nums[i], nums[j], nums[k]]))
        
        # return [list(_) for _ in result]

        # Better
        n = len(nums)
        # nums.sort()
        nums_freq = dict()
        result = set()

        for i in nums:
            nums_freq[i] = nums_freq.get(i,0) + 1

        for i in range(n):
            nums_freq[nums[i]] -= 1
            for j in range(i+1,n):
                nums_freq[nums[j]] -= 1

                target = -(nums[i] + nums[j]) 
                if target in nums_freq:
                    if nums_freq[target] > 0:
                        result.add(tuple(sorted([nums[i], nums[j], target])))
                nums_freq[nums[j]] += 1
            nums_freq[nums[i]] += 1
        return [list(_) for _ in result]




