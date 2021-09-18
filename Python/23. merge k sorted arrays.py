'''
Source: https://leetcode.com/problems/merge-k-sorted-lists/
Author: Vishal Prabhachandar
Date: 2021-August-05

Time complexity: O(nlogn)
Space complexity: O(n)  
'''


# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def mergeKLists(self, lists):
        '''
        merge k sorted linked lists

        :param  lists: list of list of ListNode objects
        :return start: ListNode object
        '''

        # brute force approach
        elements = []
        start = head = ListNode()
        for values in lists:
            while values:
                elements.append(values.val)
                values = values.next
        for element in sorted(elements):
            head.next = ListNode(element)
            head = head.next
        return start.next

        '''
        # priority queue approach
        head = pointer = ListNode()
        q = PriorityQueue()
        for element in lists:
            if element:
                q.put((element.val, element))
        while not q.empty():
            val, node = q.get()
            pointer.next = ListNode(val)
            pointer = pointer.next
            node = node.next
            if node:
                q.put((node.val, node))
        return head.next
        '''