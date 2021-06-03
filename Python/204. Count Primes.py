'''
Source: https://leetcode.com/problems/count-primes/
Author: Vishal Prabhachandar
Date: 2021-June-03

Time complexity: O(√nloglogn)
Space complexity: O(n)  
'''


class Solution:
    def countPrimes(self, n: int) -> int:
        '''
        return a count of the prime numbers less than n

        :param  n: integer
        :return count: integer
        '''
        # returning 0 primes for n < 3
        if n < 3:
            return 0
        # creating array of 1's
        array = [1] * n
        # setting numbers 0 and 1 as 0, as they are not prime
        array[0] = array[1] = 0
        # Sieve of Eratosthenes
        for index in range(2, int(n ** 0.5)+1,1):
            if array[index]:
                array[index*index:n:index] = [0] * len(array[index*index:n:index])
        return sum(array)


        # Brute force approach 
        # Time complexity: O(n*√n)
        # Space complexity: O(1)
        # count = 0
        # n = 11
        # for value in range(n,1,-1):
        #     check = 2
        #     while(check < sqrt(value)):
        #         if(value%check == 0):
        #             break
        #         else:
        #             check += 1
        #     if check > int(sqrt(value)):
        #         count += 1
        # print(count)
