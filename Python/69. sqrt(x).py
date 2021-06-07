'''
Source: https://leetcode.com/problems/sqrtx/
Author: Vishal Prabhachandar
Date: 2021-June-07

Time complexity: O(logn)
Space complexity: O(1)  
'''


class Solution:
    def mySqrt(self, x: int) -> int:
        '''
        return the sqrt of x

        :param  x: integer
        :return integer
        '''
        # base coditions
        if x == 0 or x == 1:
            return x
        start = 1
        end = x
        # binary search approach
        while start <= end:
            mid = (start + end)//2
            if mid*mid <= x < (mid + 1)*(mid + 1):
                return mid
            elif x < mid * mid:
                end = mid
            else:
                start = mid
        
        # build in function solution 
        # sqrt = int(x ** 0.5)
        # return sqrt 