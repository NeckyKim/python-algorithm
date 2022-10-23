# 5-1. 여러 가지 정렬 방법



# 배열 내 정렬
a = [2, 5, 1, 4, 3]
print(sorted(a))



# 문자열 정렬
b = "bcade"
print("".join(sorted(b)))



# 제자리 정렬(In-place Sort): 입력을 출력으로 덮어 쓰기 때문에 별도의 추가 공간이 필요하지 않음
c = [2, 5, 1, 4, 3]
c.sort()
print(c)



# 원소의 길이를 순서로 정렬
d = ["ccc", "aaaa", "d", "bb"]
print(sorted(d, key=len))



# 함수를 이용해 키를 정의하는 방법
## 예) 첫 문자열(s[0])과 마지막 문자열(s[-1])을 순으로 정렬하도록 지정
e = ["cde", "cfc", "abc"]

def myFunction(s):
    return s[0], s[-1]

print(sorted(e))
print(sorted(e, key=myFunction))