'''
Source: https://leetcode.com/problems/reverse-linked-list/
Author: Vishal Prabhachandar
Date: 2022-Jan-03

Time complexity: O(n)
Space complexity: O(1)  
'''


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
      # iterative approach
        current = None 
        while head:
            temp = head 
            head = head.next
            temp.next = current
            current = temp 
        return current
        
        #return self.recursionReverse(head, None)
    
    # recursion approach
    # def recursionReverse(self, current, previous=None):
    #     if current == None:
    #         return previous
    #     temp = current.next
    #     current.next = previous
    #     return self.recursionReverse(temp, current)
