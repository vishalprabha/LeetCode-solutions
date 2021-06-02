'''
Source: https://leetcode.com/problems/plus-one/
Author: Vishal Prabhachandar
Date: 2021-June-02

Time complexity: O(n)
Space complexity: O(1)  
'''


class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        '''
        returning with 1 added to head of array with only single digit elements

        :param  digits: List of integers
        :return digits: List of integers
        '''
        for index in range(len(digits)-1, -1, -1):
            digits[index] = digits[index] + 1 
            # replacing index with 0 as we are dealing with single digits
            if(digits[index] > 9):
                digits[index] = 0
            else:
                break
        # inserting 1 to the list if first index is 0 after carry
        if(digits[0] == 0):
                digits.insert(0,1)
        return digits