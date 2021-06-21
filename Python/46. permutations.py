'''
Source: https://leetcode.com/problems/permutations/
Author: Vishal Prabhachandar
Date: 2021-June-21

Time complexity: O(n^2*n!)
Space complexity: O(n!)  
'''


class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        '''
        return all permutations

        :param  nums: List of integers
        :return result: List of List integer
        '''
        result = []
        self.dfs(nums, [], result)
        return result

    def dfs(self, nums, path, result):
        if not nums:
            result.append(path)
            # return # backtracking
        for i in range(len(nums)):
            self.dfs(nums[:i]+nums[i+1:], path+[nums[i]], result)