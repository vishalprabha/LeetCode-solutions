'''
Source: https://leetcode.com/problems/reverse-integer/
Author: Vishal Prabhachandar
Date: 2021-June-20

Time complexity: O(n)
Space complexity: O(1)  
'''


class Solution:
    def reverse(self, x: int) -> int:
        '''
        reverse the integer

        :param  x: integer
        :return x: integer
        '''
        # constraint
        cons = 2**31
        # handling negative values
        if x < 0:
            x = int(str(x*-1)[::-1])
            x *= -1
        else:
            x = int(str(x)[::-1])
        # return based on constraint
        if x > (cons-1) or x < -cons:
            return(0)
        else:
            return(x)