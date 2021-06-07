'''
Source: https://leetcode.com/problems/kth-largest-element-in-an-array/
Author: Vishal Prabhachandar
Date: 2021-June-07

Time complexity: O(n)
Space complexity: O(n)  
'''


from heapq import heappush, heappop, heapify
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        '''
        return the kth largest element in an array

        :param  nums: List of integers
        :param  k: integer
        :return integer
        '''
        # quick select approach
        if not nums: return 
        # picking a random pivot
        pivot = random.choice(nums)
        '''
        |----------------------|-------------------------|
            left_set        middle_set      rigth_set
        '''
        right_set = [ele for ele in nums if ele > pivot]
        middle_set = [ele for ele in nums if ele == pivot]
        left_set = [ele for ele in nums if ele < pivot]
        
        right_length = len(right_set)
        middle_length = len(middle_set)
        # checking if k will fall in right_set
        if k <= right_length:
            return self.findKthLargest(right_set,k)
        # checking if k will fall in left_set
        if k > right_length + middle_length:
            return self.findKthLargest(left_set,k-right_length-middle_length)
        else:
            return middle_set[0]



        '''
        min heap approach 
        Time complexity: O((n-k)log(n))
        Space complexity: O(n)
        '''
        # heap = nums
        # # creating a heap
        # heapify(heap)
        # # popping n-k elements 
        # for elements in range(len(nums)-k):
        #     heappop(heap)
        # return heappop(heap)