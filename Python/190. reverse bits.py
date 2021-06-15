'''
Source: https://leetcode.com/problems/reverse-bits/
Author: Vishal Prabhachandar
Date: 2021-June-15

Time complexity: O(1)
Space complexity: O(1)  
'''


class Solution:
    def reverseBits(self, n: int) -> int:
        '''
        returning the reverse of n

        :param  n: 32 bit unsigned integer
        :return rev: 32 bit unsigned integer
        '''
        rev = 0
        for itr in range(32):
            # left shift rev to add new bits
            rev = rev << 1
            # xor with rev the rightmost bit of n
            rev = rev ^ (n & 1)
            # right shift n
            n = n >> 1
            
        return rev


