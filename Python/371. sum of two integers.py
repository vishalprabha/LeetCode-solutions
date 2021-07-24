'''
Source: https://leetcode.com/problems/sum-of-two-integers/
Author: Vishal Prabhachandar
Date: 2021-June-24

Time complexity: O(n)
Space complexity: O(1)  
'''


class Solution(object):
    def getSum(self, a, b):
        '''
        returning the spiral order of a matrix

        :param  a: integer
        :param  b: integer
        :return  integers
        '''
        mask = 0xffffffff
        while b!= 0:
            carry = (a&b) & mask
            sum = (a^b) & mask
            a = sum
            b = carry << 1
        # 32 bits integer max
        MAX = 0x7FFFFFFF
        return a if a <= MAX else ~(a^mask)