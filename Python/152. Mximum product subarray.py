'''
Source: https://leetcode.com/problems/maximum-product-subarray/
Author: Vishal Prabhachandar
Date: 2021-July-18

Time complexity: O(n)
Space complexity: O(1)  
'''


class Solution(object):
    def maxProduct(self, nums):
        '''
        return maximum product subarray

        :param  nums: list of integers
        :return maximum: integer
        '''
        maximum = nums[0]
        product = 1
        for index in range(len(nums)):
            product *= nums[index]
            maximum = max(product, maximum)
            if product == 0:
                product = 1
        product = 1
        for index in range(len(nums)-1,-1,-1):
            product*=nums[index]
            maximum = max(product, maximum)
            if product == 0:
                product = 1

        return maximum