'''
Source: https://leetcode.com/problems/merge-sorted-array/
Author: Vishal Prabhachandar
Date: 2021-June-07

Time complexity: O(m+n)
Space complexity: O(1)  
'''


class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        '''
        merge the sorted array in num1

        :param  nums1: list of integers
        :param  nums2: list of integers
        :param  m: length of nums1
        :param  n: length of nums2
        :return none 
        '''
        
        # reverse approach
        while m > 0 and n > 0:
            if nums1[m-1] > nums2[n-1]:
                nums1[m+n-1] = nums1[m-1]
                m -= 1
            else:
                nums1[m+n-1] = nums2[n-1]
                n -= 1
        # adding the remaining elements    
        if n > 0:
            nums1[:n] = nums2[:n]
            
        # built in function appraoch
        # nums1[m:m+n] = nums2[:n]
        # nums1 = nums1.sort()