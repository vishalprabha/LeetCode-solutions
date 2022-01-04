'''
Source: https://leetcode.com/problems/merge-two-sorted-lists/
Author: Vishal Prabhachandar
Date: 2021-August-02

Time complexity: O(n)
Space complexity: O(1)  
'''


# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def mergeTwoLists(self, l1, l2):
        '''
        merge two sorted linked list

        :param  l1: singly-linked list
        :param  l2: singly-linked list
        :return start: head of singly linked list
        '''
        start = current = ListNode()
        while l1 and l2:
            if l1.val < l2.val:
                current.next = l1
                l1 = l1.next
            else:
                current.next = l2
                l2 = l2.next
            current = current.next
        current.next = l1 or l2
        return start.next

        # recursion approach
        if list1 is None:
            return list2
        if list2 is None:
            return list1
        
        if list1.val <= list2.val:
            list1.next = self.mergeTwoLists(list1.next, list2)
            return list1
        else:
            list2.next = self.mergeTwoLists(list1, list2.next)
            return list2