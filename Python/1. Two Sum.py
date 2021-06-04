'''
Source: https://leetcode.com/problems/two-sum/
Author: Vishal Prabhachandar
Date: 2021-June-03

Time complexity: O(n)
Space complexity: O(n)  
'''


from collections import defaultdict
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        '''
        returning index of two elements in nums with target sum

        :param  nums: List of integers
        :param  target: integer
        :return output: List of integers
        '''
        # one pass solution
        # defaultdict from collections
        dict = defaultdict(int)
        output = []
        for index, value in enumerate(nums):
            diff = target - value
            # ignoring same index values
            if diff in dict and dict[diff] != index:
                output = index, dict[diff]
            else:
                dict[value] = index 
        return output
    
        # two pass solution
        # dict = defaultdict(list)
        # output = []
        # # creating the hash table
        # for index, value in enumerate(nums):
        #     dict[value] += [index]
        # for index, value in enumerate(nums):
        #     diff = target - value
        #     if diff in dict:
        #         # ignoring same index values
        #         if((len(dict[diff]) == 1 and index != dict[diff][0])):
        #             output = index,dict[diff][0]
        #             break
        #         # handling edge case if multiple same values in nums
        #         elif(len(dict[diff]) > 1):
        #             # setting the second element of value in hash table
        #             output = index,dict[diff][1]
        #             break
        # return output
        