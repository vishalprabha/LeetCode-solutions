'''
Source: https://leetcode.com/problems/counting-bits/
Author: Vishal Prabhachandar
Date: 2021-July-25

Time complexity: O(n)
Space complexity: O(n)  
'''


class Solution(object):
    def countBits(self, n):
        '''
        returning the bits in a range

        :param  n: integer
        :return counter: list of integers
        '''
        counter = [0]
        for index in range(1, n+1):
            counter.append(counter[index >> 1] + (index & 1))
        return counter
            
