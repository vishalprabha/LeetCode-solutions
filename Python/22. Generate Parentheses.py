'''
Source: https://leetcode.com/problems/generate-parentheses/
Author: Vishal Prabhachandar
Date: 2021-June-23

Time complexity: O(4^n/√n)
Space complexity: O(4^n/√n)  
'''



class Solution:
    def generateParenthesis(self, n: int) -> str:
        '''
        return all generated parentheses

        :param  n: integer
        :return answer: string
        '''
        answer = []
        def backtrack(list = [], left = 0, right = 0):
            if len(list) == 2 * n:
                answer.append("".join(list))
                return
            if left < n:
                list.append("(")
                backtrack(list, left+1, right)
                list.pop()
            if right < left:
                list.append(")")
                backtrack(list, left, right+1)
                list.pop()
        backtrack()
        return answer

obj = Solution()
print(obj.generateParenthesis(3))