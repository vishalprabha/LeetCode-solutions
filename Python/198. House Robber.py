'''
Source: https://leetcode.com/problems/house-robber/
Author: Vishal Prabhachandar
Date: 2021-June-05

Time complexity: O(n)
Space complexity: O(1)  
'''


class Solution:
    def rob(self, nums: List[int]) -> int:
        '''
        return the max amount that can be robbed

        :param  nums: list of integers
        :return curr: integer
        '''
        # solution using bottom-up DP approach
        # variable to hold the previous [i-2] value,
        prev = 0
        # variable to hold the previous [i-1] value
        curr = 0
        for index in range(len(nums)):
            temp = curr
            # finding the value to maximize output
            curr = max(prev + nums[index], curr)
            prev = temp
        return curr