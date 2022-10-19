# 6-6. 가장 긴 팰린드롬 부분 문자열



class Solution:

    # 중앙을 중심으로 확장하는 풀이
    ## 슬라이딩 윈도우와 투 포인터를 이용

    def longestPalindrome(word: str):

        # 팰린드롬 판별 및 투 포인터 확장
        def expand(left: int, right: int):
            
            # 팰린드롬 판별
            while left >= 0 and right < len(word) and word[left] == word[right]:
                
                # 투 포인터를 확장(left를 왼쪽으로, right를 오른쪽으로 이동)
                left = left - 1
                right = right + 1

            return word[left + 1:right]

        # 해당 사항이 없을 때 빠르게 리턴
        ## 예외 처리 케이스: 문자열 길이가 1이거나 뒤집어도 동일한 문자열일 때
        if len(word) < 2 or word == word[::-1]:
            return word

        result = ""

        # 슬라이딩 윈도우 우측으로 이동
        for i in range(len(word) - 1):
            result = max(
                result,
                expand(i, i + 1),   # 2칸 슬라이딩 윈도우 확장
                expand(i, i + 2),   # 3칸 슬라이딩 윈도우 확장
                key=len
            )

        return result



word = "babadeefffee"
print(Solution.longestPalindrome(word))