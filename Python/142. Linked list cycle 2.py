'''
Source: https://leetcode.com/problems/linked-list-cycle-ii/
Author: Vishal Prabhachandar
Date: 2021-January-15

Time complexity: O(n)
Space complexity: O(1)  
'''

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        '''
        detect linked list entry point

        :param  head: ListNode object
        :return head: ListNode object
        '''
        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                break
        else:
            return None
        
        while head != slow:
            head = head.next
            slow = slow.next
            
        return head