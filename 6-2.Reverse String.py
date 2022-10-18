# 6-2. 문자열 뒤집기



from typing import List

class Solution:

    # 풀이 1. 투 포인터를 이용한 스왑

    def reverseString(x: List[str]):
        left = 0
        right = len(x) - 1

        while left < right:
            x[left], x[right] = x[right], x[left]

            left = left + 1
            right = right - 1



    # 풀이 2. 파이썬다운(?) 방식
    ## 위 방식보다 조금 빠름

    def reverseStringInPythonWay(x: List[str]):
        x.reverse()



    # 풀이 3. 슬라이싱 사용

    def reverseStringWithSlicing(x: List[str]):
        x[:] = x[::-1]



sample = ["y", "u", "r", "i"]
print(sample)
Solution.reverseString(sample)
print(sample)

sample = ["y", "e", "n", "a"]
print(sample)
Solution.reverseStringInPythonWay(sample)
print(sample)

sample = ["c", "h", "a", "e", "w", "o", "n"]
print(sample)
Solution.reverseStringWithSlicing(sample)
print(sample)