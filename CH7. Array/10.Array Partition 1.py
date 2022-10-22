# 10. 배열 파티션 1
## n개의 페어를 이요한 min(a, b)의 합으로 만들 수 있는 가장 큰 수를 출력하라



from typing import List

class Solution:

    # 풀이 1. 오름차순 풀이

    def arrayPairSum1(numbers: List[int]):
        sum = 0
        pair = []
        numbers.sort()

        for i in numbers:
            # 앞에서부터 오름차순으로 페어를 만들어서 합 계산
            pair.append(i)

            # 페어가 생성되면 페어의 최소값을 sum에 더함
            if len(pair) == 2:
                sum = sum + min(pair)

                # 최소값을 더하면 페어를 초기화
                pair = []

        return sum

    # 풀이 2. 짝수 번째 값 계산
    
    def arrayPairSum2(numbers: List[int]):
        sum = 0
        numbers.sort()
        
        for index, number in enumerate(numbers):
            # 짝수 번째 값의 합 계산
            if index % 2 == 0:
                sum = sum + number

        return sum
    
    # 풀이 3. 파이썬다운 방식
    
    def arrayPairSum3(numbers: List[int]):
        # 슬라이싱을 이용하여 짝수 번째 원소의 합을 계산
        return sum(sorted(numbers)[::2])
        
        

numbers = [1, 4, 3, 2]

print(Solution.arrayPairSum1(numbers))
print(Solution.arrayPairSum2(numbers))
print(Solution.arrayPairSum3(numbers))