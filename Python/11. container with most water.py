'''
Source: https://leetcode.com/problems/container-with-most-water/
Author: Vishal Prabhachandar
Date: 2021-July-23

Time complexity: O(n)
Space complexity: O(1)  
'''


class Solution(object):
    def maxArea(self, height):
        '''
        return most water in container

        :param  height: list of integers
        :return water: integer
        '''
        left, right = 0, len(height) - 1
        water = 0
        while left < right:
            water = max(water, (right - left)*min(height[right], height[left]))
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1
        return water