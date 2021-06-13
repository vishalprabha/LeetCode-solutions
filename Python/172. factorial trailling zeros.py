'''
Source: https://leetcode.com/problems/factorial-trailing-zeroes/
Author: Vishal Prabhachandar
Date: 2021-June-13

Time complexity: O(logn)
Space complexity: O(1)  
'''


class Solution:
    def trailingZeroes(self, n: int) -> int:
        '''
        returning trailing zeros

        :param  n: integer
        :return count: integer
        '''
        count, element = 0, 5
        while(element <= n):
            count += n // element
            element *= 5
        return count 