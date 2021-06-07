'''
Source: https://leetcode.com/problems/check-if-word-equals-summation-of-two-words/
Author: Vishal Prabhachandar
Date: 2021-June-07

Time complexity: O(n)
Space complexity: O(1)  
'''


class Solution:
    def isSumEqual(self, firstWord: str, secondWord: str, targetWord: str) -> bool:
        '''
        return check of summation of words

        :param  firstWord: string
        :param  secondWord: string
        :param  targetWord: string
        :return bool
        '''

        numFirstWord = self.intString(firstWord)
        numSecondWord = self.intString(secondWord)
        numTargetWord = self.intString(targetWord)
        
        return numFirstWord + numSecondWord == numTargetWord
    
    # helper to convert string to integer
    def intString(self, string: str) -> int:
        # calculating based on ascii value of a('97')
        intConversion = ''.join(str(ord(element)-97)for element in string)
        return int(intConversion)
            