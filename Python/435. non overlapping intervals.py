'''
Source: https://leetcode.com/problems/non-overlapping-intervals/
Author: Vishal Prabhachandar
Date: 2021-July-30

Time complexity: O(nlogn)
Space complexity: O(n)  
'''


class Solution(object):
    
    def eraseOverlapIntervals(self, intervals):
        '''
        min number of intervals

        :param  intervals: list of list of integers
        :return count: integer
        '''
        intervals.sort( key = lambda x: x[0])
        currentEnd, count = intervals[0][1], 0
        for element in intervals[1:]:
            if element[0] < currentEnd:
                count += 1
                currentEnd = min(element[1], currentEnd)
            else:
                currentEnd = element[1]
        return count