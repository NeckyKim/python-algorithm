# 12. 주식을 사고팔기 가장 좋은 시점



from typing import List
import sys

class Solution:

    # 풀이 1. 브루트 포스로 계산

    def maxProfit1_1(prices: List[int]):
        max_price = 0

        for i, price in enumerate(prices):
            for j in range(i, len(prices)):
                max_price = max(prices[j] - price, max_price)

        return max_price

    # 더 직관적인 방법
    def maxProfit1_2(prices: List[int]):
        max_price = 0
        
        for i in range(len(prices)):
            for j in range(i, len(prices)):
                max_price = max(prices[j] - prices[i], max_price)
        
        return max_price
       
    # 풀이 2. 저점과 현재 값과의 차이 계산
    
    def maxProfit2(prices: List[int]):
        profit = 0
        
        # 최소값을 가장 큰 값으로 초기화
        min_price = sys.maxsize
        
        # 최소값과 최대값을 계속 갱신
        for price in prices:
            min_price = min(min_price, price)
            profit = max(profit, price - min_price)
            
        return profit



prices = [7, 1, 5, 3, 6, 4]

print(Solution.maxProfit1_1(prices))
print(Solution.maxProfit1_2(prices))
print(Solution.maxProfit2(prices))