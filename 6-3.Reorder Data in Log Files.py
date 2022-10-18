# 6-3. 로그 파일 재정렬

## 1. 로그의 가장 앞 부분은 식별자.
## 2. 문자로 구성된 로그가 숫자 로그보다 앞에 온다.
## 3. 식별자는 순서에 영향을 끼치지 않지만, 문자가 동일한 경우 식별자 순으로 한다.
## 4. 숫자 로그는 입력 순서대로 한다.



from typing import List

class Solution:
    def reorderLogFiles(logs: List[str]):
        letters = []
        digits = []

        # 문자와 숫자를 구분
        for log in logs:

            # 숫자 여부 판별
            if log.split()[1].isdigit():
                digits.append(log)

            else:
                letters.append(log)

        # 식별자를 제외한 문자열 [1:]를 키로 하여 정렬
        # 동일한 경우 후순위로 식별자[0]를 지정해 정렬
        letters.sort(key=lambda x: (x.split()[1:], x.split()[0]))

        # 이어 붙여서 다음과 같이 리턴
        return letters + digits



sample = ["dig1 8 1 5 1", 
          "let1 art can",
          "dig2 3 6", 
          "let2 own kit dig", 
          "let3 art zero"]
print(Solution.reorderLogFiles(sample))