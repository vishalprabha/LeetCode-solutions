'''
Source: https://leetcode.com/problems/3sum/
Author: Vishal Prabhachandar
Date: 2021-July-22

Time complexity: O(n^2)
Space complexity: O(1)  
'''


class Solution(object):
    def threeSum(self, nums):
        '''
        return 3sum triplets

        :param  nums: list of integers
        :return result: list of list of integers
        '''
        lenNums = len(nums)
        result = []
        nums.sort()
        for index in range(lenNums-2):
            left = index + 1
            right = lenNums - 1
            if index > 0 and nums[index] == nums[index - 1]:
                continue
            while left < right:
                total = nums[index] + nums[left] + nums[right]
                if total == 0:
                    result.append([nums[index], nums[left], nums[right]])
                    left += 1
                    while left < right and nums[left] == nums[left - 1]:
                        left += 1
                elif total < 0:
                    left += 1
                else:
                    right -= 1
        return result