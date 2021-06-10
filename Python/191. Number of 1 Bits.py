'''
Source: https://leetcode.com/problems/valid-palindrome/
Author: Vishal Prabhachandar
Date: 2021-June-09

Time complexity: O(n)
Space complexity: O(n)  
'''


class Solution:
    def hammingWeight(self, n: int) -> int:
        '''
        returning the number of 1's in n

        :param  n: integer
        :return count: integer
        '''
        count = 0 
        # solution using bitwise-and
        while(n):
            count += n&1
            n >>= 1
        return count

        # built in function solution
        # return bin(n).count('1')