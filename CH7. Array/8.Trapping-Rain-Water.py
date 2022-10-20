# 8. 빗물 트래핑
## 높이를 입력받아 비 온 후 얼마나 많은 물이 쌓일 수 있는지 계산



from typing import List

class Solution:
    
    # 풀이 1. 투 포인터를 최대로 이동
    
    def TrappingWaterUsingTwoPointers(height: List[int]):
        if not height:
            return 0
    
        # 쌓인 물 높이 변수 초기화
        volume = 0
    
        # 투 포인터 인덱스 정의
        left = 0
        right = len(height) - 1
        
        # 좌우 기둥 최대 높이 변수 초기화
        left_max = height[left]
        right_max = height[right]
        
        while left < right:
            # 현재 최대 기둥 높이보다 높으면 새로운 높이로 선언
            left_max = max(height[left], left_max)
            right_max = max(height[right], right_max)
            
            # 오른쪽이 크면 왼쪽을 이동
            if left_max <= right_max:
                # 최대 높이와 현재 높이의 차이만큼 물 높이를 더함
                volume = volume + left_max - height[left]
                left = left + 1
            
            # 왼쪽이 크면 오른쪽을 이동
            else:
                # 최대 높이와 현재 높이의 차이만큼 물 높이를 더함
                volume = volume + right_max - height[right]
                right = right - 1
                
        return volume
    
    
    
    # 풀이 2. 스택 쌓기
    
    def TrappingWaterUsingStack(height: List[int]):
        
        stack = []
        
        # 쌓인 물 높이 변수 초기화
        volume = 0
        
        for i in range(len(height)):
            # 변곡점을 만나는 경우
            while stack and height[i] > height[stack[-1]]:
                # 스택에서 꺼냄
                top = stack.pop()
                
                if not len(stack):
                    break
                
                # 이전과의 차이만큼 물 높이 처리
                distance = i - stack[-1] - 1
                waters = min(height[i], height[stack[-1]]) - height[top]
                
                volume = volume + distance * waters

            stack.append(i)
            
        return volume
    
    
    
height = [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]
print(Solution.TrappingWaterUsingTwoPointers(height))
print(Solution.TrappingWaterUsingStack(height))