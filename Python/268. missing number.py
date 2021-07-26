'''
Source: https://leetcode.com/problems/missing-number/
Author: Vishal Prabhachandar
Date: 2021-July-26

Time complexity: O(n)
Space complexity: O(1)  
'''


class Solution(object):
    def missingNumber(self, nums):
        '''
        return missing number

        :param  nums: list of intergers
        :return missing: integer
        '''

        # bit manipulation approach
        missing = len(nums)
        for index, element in enumerate(nums):
            missing ^= index ^ element
        return missing

        # sum of natural numbers approach
        # len_nums = len(nums)
        # sum_nums = sum(nums)
        # sum_actual = len_nums*(len_nums+1)/2
        # return sum_actual - sum_nums