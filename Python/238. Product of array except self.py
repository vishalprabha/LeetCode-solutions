'''
Source: https://leetcode.com/problems/product-of-array-except-self/
Author: Vishal Prabhachandar
Date: 2021-June-11

Time complexity: O(n)
Space complexity: O(1)  
'''

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        '''
        returning the product except self

        :param  nums: List of integers
        :return result: List of integers
        '''
        len_nums = len(nums)
        left = 1
        right = 1
        result = [1]*len_nums
        for index in range(len_nums):
            result[index] *= left
            result[len_nums - index - 1] *= right
            left *= nums[index]
            right *= nums[len_nums - index -1]
        return result
    
        '''
        Time complexity: O(n)
        Space complexity: O(n)
        '''
        
        # left_array = [1]*len_nums
        # right_array = [1]*len_nums
        # result_array = [1]*len_nums
        # for index in range(1,len_nums):
        #     left_array[index] = nums[index-1] * left_array[index-1]

        # for index in range(len_nums-2,-1,-1):
        #     right_array[index] = nums[index+1] * right_array[index+1]

        # for index in range(len_nums):
        #     result_array[index] = left_array[index] * right_array[index]
        # return result_array