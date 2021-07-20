'''
Source: https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/
Author: Vishal Prabhachandar
Date: 2021-July-20

Time complexity: O(logn)
Space complexity: O(1)  
'''


class Solution:
    def findMin(self, nums: List[int]) -> int:
        '''
        return minimum in rotated array

        :param  nums: list of integers
        :return integer
        '''
        left, right = 0, len(nums) - 1
        while left < right:
            mid = (left + right)//2
            if nums[mid] < nums[right]:
                right = mid
            else:
                left = mid + 1
        return nums[left]
            