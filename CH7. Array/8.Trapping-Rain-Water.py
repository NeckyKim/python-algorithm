# 8. 빗물 트래핑
## 높이를 입력받아 비 온 후 얼마나 많은 물이 쌓일 수 있는지 계산



from typing import List

class Solution:
    
    # 풀이1. 투 포인터를 최대로 이동
    
    def TrappingWaterWithTwoPointers(height: List[int]):
        if not height:
            return 0
    
        # 물 높이 변수 초기화
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
                volume = volume + left_max - height[left]
                left = left + 1
            
            # 왼쪽이 크면 오른쪽을 이동
            else:
                volume = volume + right_max - height[right]
                right = right - 1
                
            print(height[left_max], height[right_max])
                
        return volume
    

height = [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]
print(Solution.TrappingWaterWithTwoPointers(height))