'''
Source: https://leetcode.com/problems/insert-interval/
Author: Vishal Prabhachandar
Date: 2021-July-27

Time complexity: O(n)
Space complexity: O(1)  
'''


class Solution(object):
    def insert(self, intervals, newInterval):
        '''
        returning combined interval

        :param  intervals: list of list of integers
        :param  newInterval: list of integers
        :return result: list of list of integers
        '''
        result,index = [], -1
        for index, (x,y) in enumerate(intervals):
            if y < newInterval[0]:
                result.append([x,y])
            elif newInterval[1] < x:
                index -= 1
                break
            else:
                newInterval[0] = min(newInterval[0], x)
                newInterval[1] = max(newInterval[1], y)
                
        return result + [newInterval] + intervals[index+1:]
                