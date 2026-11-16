"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        intervals.sort(key = lambda x: x.start)

        for i in range(1, len(intervals)):
            start_a, end_a = intervals[i-1].start, intervals[i-1].end
            start_b, end_b = intervals[i].start, intervals[i].end

            if start_a < end_b and start_b < end_a:
                return False
        
        return True
