class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        l = 0
        r = 0
        n = len(fruits)
        max_fruits = 0
        fruit_freq = {}

        while r < n:
            # Add
            fruit_freq[fruits[r]] = fruit_freq.get(fruits[r],0) + 1
            # print(fruit_freq)

            # Invalid
            if len(fruit_freq) > 2:
                fruit_freq[fruits[l]] -= 1
                if fruit_freq[fruits[l]] == 0:
                    fruit_freq.pop(fruits[l])
                l += 1
            
            # Valid:
            if len(fruit_freq) <= 2:
                max_fruits = max(max_fruits, r-l+1)
        
            r+= 1
        return max_fruits

#  l r
# [1,2,1]
# {
#   1: 
#
# }
# [1,2,3,2,2]
# {
#     1: 1
#     2: 1
#     3: 1
# }