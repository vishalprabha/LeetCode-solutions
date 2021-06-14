'''
Source: https://leetcode.com/problems/intersection-of-two-linked-lists/
Author: Vishal Prabhachandar
Date: 2021-June-14

Time complexity: O(n)
Space complexity: O(1)  
'''


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        '''
        return the intersection node of two linked list

        :param  headA: root node of linked list A
        :param  headB: root node of linked list B
        :return ListNode
        '''
        linkA, linkB = headA, headB
        while ( linkA != linkB):
            linkA = headB if not linkA else linkA.next
            linkB = headA if not linkB else linkB.next
        return linkA