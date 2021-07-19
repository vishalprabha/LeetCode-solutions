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
        # max min approach
        maxProduct, minProduct, result = nums[0], nums[0], nums[0]
        for index in range(1, len(nums)):
            temp_maxProduct = max(nums[index], maxProduct*nums[index], minProduct*nums[index])
            temp_minProduct = min(nums[index], maxProduct*nums[index], minProduct*nums[index])
            maxProduct = temp_maxProduct
            minProduct = temp_minProduct
            result = max(maxProduct, result)
        return result

        # two pass approach
        # maximum = nums[0]
        # product = 1
        # for index in range(len(nums)):
        #     product *= nums[index]
        #     maximum = max(product, maximum)
        #     if product == 0:
        #         product = 1
        # product = 1
        # for index in range(len(nums)-1,-1,-1):
        #     product*=nums[index]
        #     maximum = max(product, maximum)
        #     if product == 0:
        #         product = 1

        # return maximum