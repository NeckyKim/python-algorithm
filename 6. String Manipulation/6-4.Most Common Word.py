# 6-4. 가장 흔한 단어
## 마침표, 쉼표는 무시



import collections
import re
from typing import List

class Solution:
    
    # 풀이. 리스트 컴프리헨션, Counter 객체 사용
    
    def mostCommonWords(paragraph: str, banned: List[str]):
        words = [
            # 문자가 아닌 모든 문자를 공백으로 치환
            word for word in re.sub(r"[^\w]", " ", paragraph).lower().split()
            
            # 금지된 단어가 없으면 수행
            if word not in banned
        ]

        counts = collections.Counter(words)

        # 가장 흔한게 등장하는 단어의 첫 번째 인덱스 리턴
        ## most_common(1): 가장 흔하게 등장하는 단어를 추출함, ex.) [('ball', 2)]
        ## most_common(1)[0][0]: 이 중에서 첫 번째 인덱스의 키를 추출
        return counts.most_common(1)[0][0]



# 문장
paragraph = "Bob hit a ball, the bit BALL flew far after it was hit."

# 금지된 단어
banned = ["hit"]

print(Solution.mostCommonWords(paragraph, banned))
