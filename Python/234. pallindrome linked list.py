'''
Source: https://leetcode.com/problems/palindrome-linked-list/
Author: Vishal Prabhachandar
Date: 2021-June-25

Time complexity: O(n)
Space complexity: O(1)  
'''


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        '''
        check for palindrome in linked list

        :param  head: first node of singly linked list
        :return boolean
        '''

        # jumping to reach hald way point
        fast = slow = head 
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        # in-place reversing
        node = None
        fast = head
        while slow:
            temp = slow.next
            slow.next = node
            node = slow
            slow = temp
        # comparison
        while node:
            if node.val != fast.val:
                return False
            node = node.next
            fast = fast.next
        
        return True 