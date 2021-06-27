'''
Source: https://leetcode.com/problems/roman-to-integer/
Author: Vishal Prabhachandar
Date: 2021-June-27

Time complexity: O(n)
Space complexity: O(1)  
'''


class Solution:
    def romanToInt(self, s: str) -> int:
        '''
        convert roman number to interger

        :param  s: string
        :return total: integer
        '''
        len_s = len(s)
        dict = {
            "I" : 1,
            "V" : 5,
            "X" : 10,
            "L" : 50,
            "C" : 100,
            "D" : 500,
            "M" : 1000
        }
        total = 0
        count = 0
        while ( count < len_s - 1):
            if dict[s[count]] < dict[s[count + 1]]:
                total += dict[s[count + 1]] - dict[s[count]]
                count += 2
            else:
                total += dict[s[count]]
                count += 1
        if count < len_s:
            total += dict[s[count]]
        return(total)