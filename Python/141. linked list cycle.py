'''
Source: https://leetcode.com/problems/linked-list-cycle/
Author: Vishal Prabhachandar
Date: 2021-August-01

Time complexity: O(n)
Space complexity: O(1)  
'''


# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def hasCycle(self, head):
        '''
        check for cycle in linked list

        :param  head: ListNode
        :return boolean
        '''
        slow = fast = head
        while fast and fast.next != None:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                return True
        
        return False
            