class Solution:
    def maxArea(self, heights: List[int]) -> int:
        # Brute Force = O(n2), O(1)
        # min(heights) * distance between area
        # distance = r - l

        n = len(heights)
        l = 0
        r = n -1
        area = -1

        while l < r:
            min_height = min(heights[l], heights[r])
            length = r - l 
            water_trapped = min_height * length
            area = max(area, water_trapped)

            if min_height == heights[l]:
                l += 1
            else:
                r -= 1
        return area

        