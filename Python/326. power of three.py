'''
Source: https://leetcode.com/problems/power-of-three/
Author: Vishal Prabhachandar
Date: 2021-June-11

Time complexity: O(logn)
Space complexity: O(1)  
'''

class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        # return True if power of 3
        if n < 1:
            return False

        while(True):
            if n%3 == 0:
                n = n // 3
                if n == 1:                    
                    return True
            else:
                break
        return False
        