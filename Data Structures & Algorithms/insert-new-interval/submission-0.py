class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:

        n = len(intervals)
        i = 0
        result = []
        
        # 3 portions:
        # Intervals that end before our newInteral starts
        # Intervals that overlap with our newInterval
        # Intervals that start after the merging

        # 1. intervals[i][1] < newInteral[0]

        while i < n and intervals[i][1] < newInterval[0]:
            result.append(intervals[i])
            i += 1
        
        while i < n and intervals[i][0] <= newInterval[1] and newInterval[0] <= intervals[i][1]:
            newInterval[0] = min(intervals[i][0], newInterval[0])
            newInterval[1] = max(intervals[i][1], newInterval[1])
            
            i += 1
        result.append(newInterval)

        while i < n:
            result.append(intervals[i])
            i += 1
        return result
        


