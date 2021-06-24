'''
Source: https://leetcode.com/problems/remove-duplicates-from-sorted-array/
Author: Vishal Prabhachandar
Date: 2021-June-24

Time complexity: O(n)
Space complexity: O(1)  
'''


class Solution:
    def removeDuplicates(self, nums: int) -> int:
        '''
        remove duplicates in sorted array

        :param  nums: List of integers
        :return counter: integer
        '''
        # built in function solution
        # nums[:] = sorted(set(nums))
        # return len(nums)
        
        # comparing elements nearby
        counter = 1
        for index in range(len(nums) - 1):
            if nums[index] != nums[index+1]:
                nums[counter] = nums[index+1]
                counter += 1
        
        return counter