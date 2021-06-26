'''
Source: https://leetcode.com/problems/delete-node-in-a-linked-list/
Author: Vishal Prabhachandar
Date: 2021-June-26

Time complexity: O(1)
Space complexity: O(1)  
'''


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def deleteNode(self, node):
        '''
            delete node from singly linked list

            :param  node: ListNode
            :return : None
        '''
        node.val = node.next.val
        node.next = node.next.next