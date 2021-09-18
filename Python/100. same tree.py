'''
Source: https://leetcode.com/problems/same-tree/solution/
Author: Vishal Prabhachandar
Date: 2021-September-18

Time complexity: O(n)
Space complexity: O(n)  
'''


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    '''
        remove duplicates in sorted array

        :param  nums: List of integers
        :return counter: integer
    '''
    # recursive solution
    # Time complexity: O(N) where is N is the number of nodes in a tree
    # Space complexity: O(N) if the tree is imbalanced
    # def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
    #     if p and q:
    #         return p.val == q.val and self.isSameTree(p.right,q.right) and  self.isSameTree(p.left, q.left)
    #     else:
    #         return p == q
    # DFS solution 
    # Time complexity: O(N) where is N is the number of nodes in a tree
    # Space complexity: O(N) if the tree is imbalanced  
    # def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
    #     stack = [(p, q)]
    #     while stack:
    #         n1, n2 = stack.pop()
    #         if n1 and n2 and n1.val == n2.val:
    #             stack.append((n1.right, n2.right))
    #             stack.append((n1.left, n2.left))
    #         elif not n1 and not n2:
    #             continue
    #         else:
    #             return False
    #     return True
    # BFS solution 
    # Time complexity: O(N) where is N is the number of nodes in a tree
    # Space complexity: O(N) if the tree is imbalanced  
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        queue = [(p, q)]
        while queue:
            node1, node2 = queue.pop(0)
            if not node1 and not node2:
                continue
            elif not node1 or not node2:
                return False
            else:
                if node1.val != node2.val:
                    return False
                queue.append((node1.left, node2.left))
                queue.append((node1.right, node2.right))
        return True
