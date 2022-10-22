# 9. 세 수의 합
## 배열을 입력받아 합으로 0을 만들 수 있는 3개의 엘리먼트를 출력



from typing import List

class Solution:

    # 풀이 1. 브루트 포스로 계산

    def threeSum(numbers: List[int]):
        results = []
        numbers.sort()

        # 브루트 포스 n^3 반복
        for i in range(len(numbers) - 2):
            # 중복된 값은 건너뛰기
            if i > 0 and numbers[i] == numbers[i - 1]:
                continue

            for j in range(i + 1, len(numbers) - 1):
                # 중복된 값은 건너뛰기
                if j > i + 1 and numbers[j] == numbers[j - 1]:
                    continue

                for k in range(j + 1, len(numbers)):
                    # 중복된 값은 건너뛰기
                    if k > j + 1 and numbers[k] == numbers[k - 1]:
                        continue

                    # 세 수의 합이 0인지 확인
                    if numbers[i] + numbers[j] + numbers[k] == 0:
                        results.append([numbers[i], numbers[j], numbers[k]])

        return results

    # 풀이 2. 투 포인터로 합 계산

    def threeSumUsingTwoPointers(numbers: List[int]):
        results = []
        numbers.sort()

        for i in range(len(numbers) - 2):
            # 중복된 값은 건너뛰기
            if i > 0 and numbers[i] == numbers[i - 1]:
                continue

            # 간격을 좁혀가며 합 sum 계산
            left = i + 1
            right = len(numbers) - 1

            while left < right:
                sum = numbers[i] + numbers[left] + numbers[right]

                # 합이 0보다 작으면 왼쪽 포인터를 오른쪽으로 이동
                if sum < 0:
                    left = left + 1

                # 합이 0보다 크면 오른쪽 포인터를 왼쪽으로 이동
                elif sum > 0:
                    right = right - 1

                # 합이 0이면 배열에 넣고 스킵 처리
                else:
                    results.append([numbers[i], numbers[left], numbers[right]])

                    # 왼쪽 포인터의 오른쪽에 동일한 값이 있으면 오른쪽으로 이동시켜 스킵 처리
                    while left < right and numbers[left] == numbers[left + 1]:
                        left = left + 1

                    # 오른쪽 포인터의 왼쪽에 동일한 값이 있으면 왼쪽으로 이동시켜 스킵 처리
                    while left < right and numbers[right] == numbers[right - 1]:
                        right = right - 1

                    left = left + 1
                    right = right - 1

        return results



numbers = [-1, 0, 1, 2, -1, -4]

print(Solution.threeSum(numbers))
print(Solution.threeSumUsingTwoPointers(numbers))