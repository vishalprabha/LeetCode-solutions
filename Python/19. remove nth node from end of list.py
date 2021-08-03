'''
Source: https://leetcode.com/problems/remove-nth-node-from-end-of-list/
Author: Vishal Prabhachandar
Date: 2021-August-03

Time complexity: O(n)
Space complexity: O(1)  
'''

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        '''
        merge two sorted linked list

        :param  head: ListNode object
        :param  n: integer
        :return start: ListNode object
        '''
        start = ListNode()
        start.next = head
        first = start
        second = start
        for index in range(n+1):
            first = first.next
        while first:
            first = first.next
            second = second.next
        second.next = second.next.next
        return start.next