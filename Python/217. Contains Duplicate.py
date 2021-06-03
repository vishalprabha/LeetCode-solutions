'''
Source: https://leetcode.com/problems/contains-duplicate/
Author: Vishal Prabhachandar
Date: 2021-June-03

Time complexity: O(n)
Space complexity: O(n)  
'''


from collections import defaultdict
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        '''
        return a boolean if list contains a duplicate

        :param  nums: List of integers
        :return output: boolean
        '''
        # default dict from collection
        dict = defaultdict(int)
        output = False
        for index in nums:
            dict[index] += 1
            # check if value is already present
            if dict[index] > 1:
                output = True
                break
        return output
        
        # built in set function solution
        # return len(set(nums)) < len(nums)
        
        # built in dictionary solution
        # dict = {}
        # output = False
        # for element in nums: 
        #     if element in dict:
        #         output = True
        #     else:
        #         dict[element] = 1
        # return output
        