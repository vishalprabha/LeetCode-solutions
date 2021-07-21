'''
Source: https://leetcode.com/problems/search-in-rotated-sorted-array/
Author: Vishal Prabhachandar
Date: 2021-July-21

Time complexity: O(logn)
Space complexity: O(1)  
'''


class Solution(object):
    def search(self, nums, target):
        '''
        return index of target in rotated array if present

        :param  nums: list of integers
        :return mid: integer
        '''
        low, high = 0, len(nums)-1
        while low <= high:
            mid = (low + high)//2
            if nums[mid] == target:
                return mid
            if nums[low] <= nums[mid]:
                if nums[low] <= target <= nums[mid]:
                    high = mid - 1
                else:
                    low = mid + 1
            else:
                if nums[mid] <= target <= nums[high]:
                    low = mid + 1
                else:
                    high = mid - 1
        
        return -1