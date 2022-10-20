# 7. 두수의 합
## 덧셈하여 타겟을 만들 수 있는 배열의 두 숫자 인덱스를 리턴



from typing import List

class Solution:

    # 풀이 1. 브루트 포스로 계산

    def twoSum1(nums: List[int], target: int):
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if nums[i] + nums[j] == target:
                    return [i, j]

    # 풀이 2. in을 이용한 탐색
    ## 모든 조합을 비교하지 않고, 타겟에서 첫 번째 값을 뺀 값 target - n이 존재하는지 확인

    def twoSum2(nums: List[int], target: int):
        for i, n in enumerate(nums):
            complement = target - n     # 타겟에서 첫 번째 값을 뺀 값

            if complement in nums[i + 1:]:
                return [nums.index(n), nums[i + 1:].index(complement) + (i + 1)]

    # 풀이 3. 첫 번째 수를 뺀 결과 키 조회

    def twoSum3(nums: List[int], target: int):
        nums_map = {}

        # 키와 값을 바꿔서 딕셔너리로 저장
        ## 결과 값 예시: {2: 0, 7: 1, 11: 2, 15: 3}
        for i, num in enumerate(nums):
            nums_map[num] = i

        # 타겟에서 첫 번째 수를 뺀 결과를 키로 조회
        for i, num in enumerate(nums):
            if (target - num in nums_map) and (i != nums_map[target - num]):
                return [i, nums_map[target - num]]

    # 풀이 4. 조회 구조 개선

    def twoSum4(nums: List[int], target: int):
        nums_map = {}

        # 하나의 for 문으로 통합
        for i, num in enumerate(nums):
            if target - num in nums_map:
                return [nums_map[target - num], i]
            nums_map[num] = i

    # 풀이 5. 투 포인터 이용
    ## 이 방법은 리스트가 이미 정렬된 상태에서만 사용 가능

    def twoSum4(nums: List[int], target: int):
        # 투 포인터 인덱스 정의
        left = 0
        right = len(nums) - 1

        while not left == right:            
            # 합이 타겟보다 작으면 왼쪽 포인터를 오른쪽으로 이동
            if nums[left] + nums[right] < target:
                left = left + 1

            # 합이 타겟보다 크면 오른쪽 포인터를 왼쪽으로 이동
            elif nums[left] + nums[right] > target:
                right = right - 1

            else:
                return [left, right]


nums = [2, 7, 11, 15]
target = 9

print(Solution.twoSum1(nums, target))
print(Solution.twoSum2(nums, target))
print(Solution.twoSum3(nums, target))
print(Solution.twoSum4(nums, target))