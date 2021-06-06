'''
Source: https://leetcode.com/problems/set-matrix-zeroes/
Author: Vishal Prabhachandar
Date: 2021-June-06

Time complexity: O(m*n)
Space complexity: O(1)  
'''


class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        modifying matrix in-place instead

        :param  matrix: m*n matrix of integers
        :return None
        """
        
        # check variable initializaiton
        zero_in_first_row = 0
        zero_in_first_column = 0
        # size variable initialization 
        row_size = len(matrix)
        column_size = len(matrix[0])
        
        for row_loop in range(row_size):
            for column_loop in range(column_size):
                if matrix[row_loop][column_loop] == 0:
                    # setting 0 in Beginning of row and column if 0 is encountered
                    matrix[row_loop][0] = matrix[0][column_loop] = 0
                    # checking for 0 in first row
                    if row_loop == 0:
                        zero_in_first_row = 1
                    # checking for 0 in first column 
                    if column_loop == 0:
                        zero_in_first_column = 1
        
        # based on markings from earlier pass, we mark 0's in the complete row and column starting index 1
        for row_loop in range(1,row_size):
            for column_loop in range(1,column_size):
                if matrix[row_loop][0] == 0 or matrix[0][column_loop]==0:
                    matrix[row_loop][column_loop] = 0

        # if 0 in first row, fill matrix accordingly 
        if zero_in_first_row:
            for column_loop in range(column_size):
                matrix[0][column_loop] = 0
                
        # if 0 in first column, fill matrix accordingly         
        if zero_in_first_column:
            for row_loop in range(row_size):
                matrix[row_loop][0] = 0