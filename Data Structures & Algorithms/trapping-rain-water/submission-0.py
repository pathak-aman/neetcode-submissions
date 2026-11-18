class Solution:
    def trap(self, height: List[int]) -> int:
        #
        # |
        # |.            |
        # |.            |
        # |.      |.    |
        # |   | | |.    |
        # | | | | |     |

        # Water at each building = min(leftmax, rightmax) - height[i]

        n = len(height)
        trapped_water = 0

        left_max = [0 for _ in range(n)]
        right_max = [0 for _ in range(n)]

        left_max[0] = height[0]
        for i in range(1,n):
            left_max[i] = max(left_max[i-1], height[i])

        right_max[n-1] = height[n-1]
        for i in range(n-2,-1,-1):
            right_max[i] = max(right_max[i+1], height[i])
        
        for i in range(n):
            trapped_water += min(left_max[i], right_max[i]) - height[i]

        return trapped_water
            