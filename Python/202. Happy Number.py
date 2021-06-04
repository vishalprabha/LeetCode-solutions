'''
Source: https://leetcode.com/problems/happy-number/
Author: Vishal Prabhachandar
Date: 2021-June-04

Time complexity: O(n)
Space complexity: O(n)  
'''


from collections import defaultdict
class Solution:
    def isHappy(self, n: int) -> bool:
        '''
        returning the happy number

        :param  n: integers
        :return output: boolean
        '''
        output = False
        # default dict from collection
        dict = defaultdict(int)
        while(True):
            # checking for happy
            if n == 1:
                output = True 
                break
            dict[n] = 1
            n = self.squareNumber(n)
            # checking for loop
            if n in dict:
                break
        return output
    # sum of square of digits    
    def squareNumber(self, n:int) -> int:
        square = 0
        while(n//10 >= 1):
            square += ((n%10)**2)
            n //= 10
        square += n**2
        return square