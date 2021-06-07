'''
Source: https://leetcode.com/problems/pascals-triangle/
Author: Vishal Prabhachandar
Date: 2021-June-07

Time complexity: O(numRows^2)
Space complexity: O(numRows^2)  
'''


class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        '''
        return the pascal triangle for a number

        :param  numRows: integer
        :return pascal_triangle: List of List of integers
        '''
        # initializing first
        pascal_triangle = [[1] * (i+1) for i in range(numRows)]
        # looping and updating the values based on the rule
        for out_loop in range(2, numRows):
            for inner_loop in range(1, out_loop):
                pascal_triangle[out_loop][inner_loop] = pascal_triangle[out_loop-1][inner_loop-1] \
                + pascal_triangle[out_loop-1][inner_loop]
        return pascal_triangle