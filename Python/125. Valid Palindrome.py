'''
Source: https://leetcode.com/problems/valid-palindrome/
Author: Vishal Prabhachandar
Date: 2021-June-09

Time complexity: O(n)
Space complexity: O(n)  
'''


class Solution:
    def isPalindrome(self, s: str) -> bool:
        '''
        returning if s is a valid palindrome

        :param  s: string
        :return boolean
        '''
        forward = ""
        backward = ""
        for index in range(len(s)):
            if s[index].isalnum():
                forward += s[index].lower()
        # reversing the string
        backward = forward[::-1]
        return forward == backward