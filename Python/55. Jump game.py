'''
Source: https://leetcode.com/problems/jump-game/
Author: Vishal Prabhachandar
Date: 2021-June-18

Time complexity: O(n)
Space complexity: O(1)  
'''


class Solution:
    def canJump(self, nums: List[int]) -> bool:
        '''
        return is jump is possible 

        :param  nums: List of integers
        :return boolean
        '''
        # forward approach
        jump = 0
        for index, element in enumerate(nums):
       
            if index > jump:
                return(False)
            jump = max(jump, index+element)
        return(True)

        # reverse approach
        # last_position = len(nums)-1
        # for i in range(len(nums)-2,-1,-1): 
        #     if (i + nums[i]) >= last_position: 
        #         last_position = i 
        # return(last_position == 0)

