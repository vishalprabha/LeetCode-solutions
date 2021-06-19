'''
Source: https://leetcode.com/problems/move-zeroes/
Author: Vishal Prabhachandar
Date: 2021-June-19

Time complexity: O(n)
Space complexity: O(1)  
'''


class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        '''
        move zeros in-place

        :param  nums: list of integers
        '''
        counter = 0
        # brining non zero elements forward
        for index in range(len(nums)):
            if nums[index] != 0:
                nums[counter] = nums[index]
                counter += 1
        # filling up the remaning array with zeros
        for index in range(counter, len(nums)):
            nums[index] = 0
        return(nums) 

        # brute force approach 
        # for outerLoop in range(nums.count(0)):
        #     for index in range(len(nums) - outerLoop -1):
        #         if nums[index] == 0:
        #             tmp = nums[index]
        #             nums[index] = nums[index + 1] 
        #             nums[index + 1] = tmp
        # return(nums)