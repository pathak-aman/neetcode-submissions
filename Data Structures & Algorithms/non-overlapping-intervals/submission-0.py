class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        n = len(intervals)
        intervals.sort(key=lambda x: x[1])
        result = [intervals[0]]
        remove = 0 


        # A (start_a, end_a) and B (start_b, end_b)
        # start_a < end_b and start_b < end_b

        for i in range(1,n):
            # Overlapping 
            if result[-1][0] < intervals[i][1] and intervals[i][0] < result[-1][1]:
                remove += 1
            else:
                result.append(intervals[i])
            
        return remove






        