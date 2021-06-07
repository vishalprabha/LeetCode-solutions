'''
Source: https://leetcode.com/problems/majority-element/
Author: Vishal Prabhachandar
Date: 2021-June-07

Time complexity: O(n)
Space complexity: O(n)  
'''


from collections import defaultdict
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        '''
        return majority element

        :param  nums: list of integers
        :return element: integer
        '''

        len_nums = len(nums)
        # initializing hash map
        count = defaultdict(int)
        for element in nums:
            count[element] += 1
            # check if element majority
            if(count[element] > len_nums//2):
                return element
        
        # Booyer-moore algo
        # Time complexity: O(n)
        # Space complexity: O(1)
        # count = 0 
        # element = 0
        # for num in nums:
        #     if count == 0:
        #         element = num
        #     count += 1 if element == num else -1
        # return element