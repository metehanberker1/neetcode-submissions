"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        if len(intervals) == 1:
            return 1

        starts = [interval.start for interval in intervals]
        starts.sort()
        ends = [interval.end for interval in intervals]
        ends.sort()

        res = 0
        count = 0

        s = 0
        e = 0
        
        while s < len(intervals) and e < len(intervals):
            if starts[s] < ends[e]:
                s += 1
                count += 1
            else:
                e += 1
                if count > res:
                    res = count
                count -= 1

        return count if res == 0 else res