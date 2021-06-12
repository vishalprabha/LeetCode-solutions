'''
Source: https://leetcode.com/problems/merge-two-sorted-lists/
Author: Vishal Prabhachandar
Date: 2021-June-12

Time complexity: O(m+n)
Space complexity: O(m+n)  
'''


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        '''
        return the merged list in sorted format

        :param  l1: singly linked list
        :param  l2: singly linked list
        :return dummy: merged singly linked list
        '''
        dummy = current = ListNode(0)

        while(l1.next != None and l2.next != None):
            if(l1.val <= l2.val):
                current.next = l1
                l1 = l1.next
            else:
                current.next = l2
                l2 = l2.next
            current = current.next
        current.next = l1 or l2
        return dummy.next