'''
Source: https://leetcode.com/problems/valid-anagram/
Author: Vishal Prabhachandar
Date: 2021-June-16

Time complexity: O(s+t)
Space complexity: O(s)  
'''


from collections import defaultdict
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        # if len(s) != len(t):
        #     return False
        dict = defaultdict(int)
        # creating dict for elements in s
        for element in s:
            dict[element] += 1
        output = True
        # checking if element is present and return the result
        for element in t:
            if element in dict:
                dict[element] -=1
                if dict[element] < 0:
                    output = False
                    break
            else:
                output = False
                break
        return output and sum(dict.values()) == 0
        # if the length test is done at the beginning 
        # return output