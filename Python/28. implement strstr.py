'''
Source: https://leetcode.com/problems/implement-strstr/
Author: Vishal Prabhachandar
Date: 2021-June-17

Time complexity: O(n)
Space complexity: O(1)  
'''


class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        '''
        return if needle is present in haystack

        :param  haystack: string
        :param  needle: string
        :return index: index of first matching char for needle in haystack
        '''
        # comparing using slicing operation
        for index in range(len(haystack) - len(needle)+1):
            if (haystack[index:index+len(needle)] == needle):
                return index
        
        return -1