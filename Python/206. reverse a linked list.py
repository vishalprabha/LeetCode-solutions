'''
Source: https://leetcode.com/problems/reverse-linked-list/
Author: Vishal Prabhachandar
Date: 2021-July-31

Time complexity: O(n)
Space complexity: O(1)  
'''


# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reverseList(self, head):
        '''
        reverse a linked list

        :param  head: ListNode
        :return previous: ListNode
        '''
        current = head
        previous = None
        while current:
            temp = current.next
            current.next = previous
            previous = current 
            current = temp
        
        return previous