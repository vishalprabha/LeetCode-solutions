'''
Source: https://leetcode.com/problems/maximum-subarray/
Author: Vishal Prabhachandar
Date: 2021-July-16

Time complexity: O(n)
Space complexity: O(1)  
'''

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        '''
        return largest subarray sum

        :param  nums: list of integers
        :return maximum: integer
        '''
        current = maximum = nums[0]
        for index in range(1, len(nums)):
            current = max(nums[index], current + nums[index])
            maximum = max(current, maximum)
            
        return maximum