'''
Source: https://leetcode.com/problems/fizz-buzz/
Author: Vishal Prabhachandar
Date: 2021-June-05

Time complexity: O(n)
Space complexity: O(1)  
'''


class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        '''
        return a count of the prime numbers less than n

        :param  n: integer
        :return array: list of string
        '''
        # idea based on Sieve of Eratosthenes approach
        array = []
        for index in range(1,n+1):
            array.append(str(index))
        for index in range(2,n,3):
            array[index] = "Fizz"
        for index in range(4,n,5):
            array[index] = "Buzz"
        for index in range(14,n,15):
            array[index] = "FizzBuzz"
        return array

        # string concatenation approach
        # array = []
        # for index in range(1,n+1):
        #     # checking divisibility of 3
        #     div_3 = index % 3 == 0
        #     # checking divisibility of 5
        #     div_5 = index % 5 ==0
        #     # required for string concatenation
        #     ans = ""
        #     if div_3:
        #         ans += "Fizz"
        #     if div_5:
        #         ans += "Buzz"
        #     if not ans:
        #         ans += str(index)
        #     array.append(ans)
        # return array