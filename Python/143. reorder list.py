'''
Source: https://leetcode.com/problems/reorder-list/
Author: Vishal Prabhachandar
Date: 2021-August-04

Time complexity: O(n)
Space complexity: O(1)  
'''


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: ListNode) -> None:
        '''
        reorder linked list

        :param  head: ListNode object
        :return None
        '''
        # find the middle of the list
        slow = fast = head  
        while  fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next
        
        # reverse the second half of the list
        previous, current = None, slow.next
        while current:
            temp = current.next
            current.next = previous
            previous = current
            current = temp
        slow.next = None
        
        # reorder the list
        start = head
        while previous:
            temp = start.next
            start.next = previous
            start = previous
            previous = temp
            