# 11. 자신을 제외한 배열의 곱
## 배열을 입력받아 자신을 제외한 나머지 모든 요소의 곱셈 결과가 되도록 출력하라
## 단, 나눗셈을 하지 않고 O(n)에 풀어야 함



from typing import List

class Solution:

    # 풀이. 왼쪽 곱셈 결과에 오른쪽 값을 차례대로 곱셈

    def productExceptSelf(numbers: List[int]):
        out = []
        
        # 왼쪽에 있는 값들을 곱셈
        p = 1   # p: 1 -> 1 -> 2 -> 6
        
        for i in range(0, len(numbers)):
            out.append(p)
            p = p * numbers[i]            

        # 왼쪽 곱셈 결과에 오른쪽에 값을 차례대로 곱셈 
        p = 1   # p: 1 -> 4 -> 12 -> 24
              
        for i in range(len(numbers) - 1, 0 - 1, -1):
            out[i] = out[i] * p
            p = p * numbers[i]
            
        return out

        ##  1   1   2   6
        ##  24  12  4   1
        ##  ----------------
        ##  24  12  8   6



numbers = [1, 2, 3, 4]

print(Solution.productExceptSelf(numbers))



numbers = [-1, 1, 0, -3, 3]

print(Solution.productExceptSelf(numbers))