'''
Source: https://leetcode.com/problems/intersection-of-two-arrays-ii/
Author: Vishal Prabhachandar
Date: 2021-July-12

Time complexity: O(n^2)
Space complexity: O(n)  
'''

class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        '''
        return an array which is an intersection of two arrays

        :param  nums1: list of integers
        :param  nums2: list of integers
        :return result: list of integers
        
        '''
        result = []
        for element in nums1:
            if element in nums2:
                nums2.remove(element)
                result.append(element)
                
        return result