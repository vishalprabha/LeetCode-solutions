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
        middle = self.findMiddle(head)
        # reverse the second half of the list
        reversedList = self.reverseList(middle)
        # merge the two lists
        reorderList = self.mergeList(head, reversedList)
        
        
    def findMiddle(self, head):
        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        return slow

    def reverseList(self, middle):
        start = None
        while middle:
            temp = middle.next
            middle.next = start
            start = middle
            middle = temp
        return start
    
    def mergeList(self, head, reversedList):
        start = head
        while reversedList and reversedList.next:
            temp = start.next
            start.next = reversedList
            start = temp
            
            temp = reversedList.next
            reversedList.next = start
            reversedList = temp
            