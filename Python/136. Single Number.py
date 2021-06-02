'''
Source: https://leetcode.com/problems/single-number/
Author: Vishal Prabhachandar
Date: 2021-June-02

Time complexity: O(n)
Space complexity: O(1)  
'''

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        '''
        returning the single value in nums list

        :param  nums: List of integers
        :return single: integer
        '''
        single = 0 
        # XOR to find the single number
        for value in nums:
            single ^= value
        return single

