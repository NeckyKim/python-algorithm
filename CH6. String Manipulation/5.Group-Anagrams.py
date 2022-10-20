# 5. 그룹 애너그램
## 애너그램(Anagram): 문자를 재배열하여 다른 뜻을 가진 단어로 바꾸는 것



import collections
from typing import List

class Solution:
    
    # 풀이. 정렬하여 딕셔너리에 추가
    
    def groupAnagrams(words: List[str]):
        
        # 항상 디폴트를 생성해주는 defaultdict() 사용
        anagrams = collections.defaultdict(list)
        
        for word in words:
            # 정렬하여 딕셔너리에 추가
            anagrams["".join(sorted(word))].append(word)
        
        return list(anagrams.values())
    


anagrams = ["eat", "tea", "bus", "tab", "atn", "tan", "ate", "sub", "nat", "bat"]

print(Solution.groupAnagrams(anagrams))