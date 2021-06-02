'''
Source: https://leetcode.com/problems/reverse-string/
Author: Vishal Prabhachandar
Date: 2021-June-02

Time complexity: O(n)
Space complexity: O(1)  
'''


class Solution:
    def reverseString(self, s: List[str]) -> None:
        '''
        reverse string 's' in-place  

        :param s: List of strings 
        :return None
        '''
        strLength = len(s)
        for index in range(0, strLength//2):
            s[index],s[strLength-index-1]=s[strLength-index-1],s[index]

        # alternate solution using slice notation
        # s[:] = s[::-1]
        # alternate solution using inbuilt function
        # s.reverse()