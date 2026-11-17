"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        n = len(intervals)
        ongoing = 0
        max_ongoing = 0

        start = [_.start for _ in intervals]
        end = [_.end for _ in intervals]

        start.sort()
        end.sort()

        s = 0
        e = 0

        while s < n:
            if start[s] < end[e]:
                ongoing += 1
                s += 1
            else:
                ongoing -= 1
                e += 1
            max_ongoing = max(max_ongoing, ongoing)
        return max_ongoing


        