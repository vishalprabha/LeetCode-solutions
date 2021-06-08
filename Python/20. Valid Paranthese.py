'''
Source: https://leetcode.com/problems/valid-parentheses/
Author: Vishal Prabhachandar
Date: 2021-June-08

Time complexity: O(n)
Space complexity: O(n)  
'''


class Solution:
    def isValid(self, s: str) -> bool:
        '''
        return if valid paranthese

        :param  s: string
        :return output: bool
        '''
        # base case
        if len(s) == 1:
            return False
        # initializing mapping
        reference = { ')' : '(', '}' : '{', ']' : '['}
        # stack
        tracker = []
        output = True
        for element in s:
            if element in reference.keys():
                # checking if paranthese are matching
                if len(tracker) > 0 and reference[element] == tracker[-1]:
                    tracker.pop()
                else:
                    output = False
                    break
            else:
                tracker.append(element)
                
        if len(tracker) > 0:
            output = False
        return output