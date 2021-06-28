'''
Source: https://leetcode.com/problems/best-time-to-buy-and-sell-stock/
Author: Vishal Prabhachandar
Date: 2021-June-28

Time complexity: O(n)
Space complexity: O(1)  
'''


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        '''
            max profit

            :param  prices: list of integers
            :return max: integer
        '''
        lenPrices = len(prices)
        if lenPrices < 2:
            return 0
        min, max = prices[0], 0
        for index in range(1, lenPrices):
            if( prices[index] < min):
                min = prices[index]
            elif prices[index] - min > max:
                max = prices[index] - min
            
        return max
            