# 13. 팰린드롬 연결 리스트



import collections
from typing import List

# 링크드 리스트 정의
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    
    # 풀이 1. 리스트 변환
    
    def isPalindromeUsingList(self, head: ListNode):
        q: List = []
        
        if not head:
            return True
        
        node = head
        
        # 리스트 변환
        while node is not None:
            q.append(node.val)
            node = node.next
            
        # 팰린드롬 판별
        while len(q) > 1:
            if q.pop(0) != q.pop():
                return False
            
        return True
    
    # 풀이 2. 데크를 이용한 최적화
    
    def isPalindromeUsingDeque(self, head: ListNode):
        # 데크 자료형 선언
        q: Deque = collections.deque()
        
        if not head:
            return True
        
        node = head
        
        while node is not None:
            q.append(node.val)
            node = node.next
            
        # 팰린드롬 판별
        while len(q) > 1:
            # 데크를 이용해서 양쪽에서 꺼내서 값을 비교
            if q.popleft() != q.pop():
                return False
            
        return True
    
    # 풀이 3. 런너를 이용한 우아한 풀이
    
    def isPalindromeUsingRunner(self, head: ListNode):
        # 느린 런너가 지나가는 노드를 역순으로 저장하는 연결 리스트
        reverse = None
        
        # 느린 런너와 빠른 런너의 시작점은 Head
        slow = head
        fast = head
            
        # 런너를 이용해 역순 연결 리스트 구성
        
        while fast and fast.next:
            fast = fast.next.next                                   # 빠른 런너는 2칸씩 이동
            reverse, reverse.next, slow = slow, reverse, slow.next  # 느린 런너는 1칸씩 이동
            
            
        if fast:
            slow = slow.next
            
        # 팰린드롬 여부 확인
        while reverse and reverse.val == slow.val:
            slow = slow.next
            reverse = reverse.next
            
        return not reverse


    
# 노드 생성
## 1->2->3->2->1
node1 = ListNode(1)
node2 = ListNode(2)
node3 = ListNode(3)
node4 = ListNode(2)
node5 = ListNode(1)

# 노드 간 포인터 연결
node1.next = node2
node2.next = node3
node3.next = node4
node4.next = node5

# 헤드 노드 지정
head = node1



solution = Solution()

print(solution.isPalindromeUsingList(head))
print(solution.isPalindromeUsingDeque(head))
print(solution.isPalindromeUsingRunner(head))