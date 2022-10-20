# 1. 팰린드롬 확인
## 팰린드롬(Palindrome): 앞뒤가 똑같은 단어 또는 문장



import collections
import re
from typing import Deque

class Solution:
    
    # 풀이 1. 리스트로 변환

    def isPalindrome(x: str):
        temp = []

        # 소문자로 모두 변환
        for char in x:
            if char.isalnum():
                temp.append(char.lower())

        # 팰린드롬 여부 판별
        while len(temp) > 1:
            if temp.pop(0) != temp.pop():   # 맨 앞의 문자와 맨 뒤 문자를 비교
                return False                # 하나라도 같지 않으면 False를 반환

        return True                         # 모두 같으면 True를 반환



    # 풀이 2. 데크(Deque) 자료형을 이용한 최적화
    ## 빠르게 해결 가능 

    def isPalindromeUsingDeque(x: str):
        temp = collections.deque()

        for char in x:
            if char.isalnum():
                temp.append(char.lower())

        while len(temp) > 1:
            if temp.popleft() != temp.pop():
                return False

        return True



    # 풀이 3. 슬라이싱(Slicing) 사용
    ## 더 빠르게 해결 가능

    def isPalindromeWithSlicing(x: str):
        x = x.lower()

        # 정규식으로 불필요한 문자 필터링
        x = re.sub("[^a-z0-9]", "", x)

        return x == x[::-1]



print(Solution.isPalindrome("Was it a cat I saw?"))  # 팰린드롬인 단어
print(Solution.isPalindrome("No, it's not"))        # 팰린드롬이 아닌 단어

print(Solution.isPalindromeUsingDeque("Was it a cat I saw?"))
print(Solution.isPalindromeUsingDeque("No, it's not"))

print(Solution.isPalindromeWithSlicing("Was it a cat I saw?"))
print(Solution.isPalindromeWithSlicing("No, it's not"))