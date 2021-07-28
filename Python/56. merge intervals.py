'''
Source: https://leetcode.com/problems/merge-intervals/
Author: Vishal Prabhachandar
Date: 2021-July-28

Time complexity: O(nlogn)
Space complexity: O(n)  
'''


class Solution(object):
    def merge(self, intervals):
        '''
        merge intervals

        :param  intervals: list of list of integers
        :return result: list of list of integers
        '''
        result = []
        intervals.sort(key=lambda x:x[0])
        interval = intervals[0]
        for index, (x,y) in enumerate(intervals, 1):
            if interval[1] < x:
                result.append(interval)
                interval = [x,y]
            else:
                interval[1] = max(interval[1], y)
        result.append(interval)
        return result