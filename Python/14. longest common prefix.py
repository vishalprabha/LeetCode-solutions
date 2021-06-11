
'''
Source: https://leetcode.com/problems/longest-common-prefix/
Author: Vishal Prabhachandar
Date: 2021-June-11

Time complexity: O(n)
Space complexity: O(1)  
'''

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        '''
        returning longest common prefix

        :param  strs: List of strings
        :return prefix: string
        '''
        prefix = ""
        len_strs = len(strs)
        stop_flag = False
        # iterating only for elements in first value
        for index, value in enumerate(strs[0]):
            # comparing with other words in strs
            for element in range(1, len_strs):
                if index < len(strs[element]) and value == strs[element][index]:
                    continue
                else:
                    stop_flag = True
                    break
            if stop_flag:
                break
            else:
                prefix += value
        
        return prefix