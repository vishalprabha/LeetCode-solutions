'''
Source: https://leetcode.com/problems/intersection-of-two-arrays-ii/
Author: Vishal Prabhachandar
Date: 2021-July-12

Time complexity: O(nlog(n))
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

        # two pointer approach if arrays are sorted
        nums1 = sorted(nums1)
        nums2 = sorted(nums2)
        result = []
        len_nums1 = len(nums1)
        len_nums2 = len(nums2)
        index_nums1 = 0
        index_nums2 = 0
        while index_nums1 < len_nums1 and index_nums2 < len_nums2:
            if nums1[index_nums1] < nums2[index_nums2]:
                index_nums1 += 1
            elif nums1[index_nums1] > nums2[index_nums2]:
                index_nums2 += 1
            else:
                result.append(nums1[index_nums1])
                index_nums1 += 1
                index_nums2 += 1
        return result
            


        # brute force approach
        # result = []
        # for element in nums1:
        #     if element in nums2:
        #         nums2.remove(element)
        #         result.append(element)
                
        # return result

        # inbuilt counter approach
        # c1, c2 = Counter(nums1), Counter(nums2)
        # finding intersection and returning
        # return(c1&c2).elements()

        # dictionary based approach
        # dic = {}
        # for element in nums2:
        #    dic[element] =  dic.get(element,0) + 1
        # result = []
        # for element in nums1:
        #     if element in dic and dic[element] > 0:
        #         result.append(element)
        #         dic[element] -= 1
        # return result