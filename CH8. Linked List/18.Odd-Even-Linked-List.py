# 18. 홀짝 연결 리스트
## 연결 리스트를 홀수 노드 다음에 짝수 노드가 오도록 재구성
## 공간 복잡도: O(1), 시간 복잡도: O(n)



# 링크드 리스트 정의

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    
    # 풀이 1. 값만 교환
    
    def oddEvenList(self, head: ListNode):
        # 예외 처리
        if head is None:
            return None
        
        odd = head              # 첫 번째 노드부터 시작
        even = head.next        # 두 번째 노드부터 시작
        even_head = head.next   # 홀수 노드의 마지막을 짝수 노드의 처음과 이어주기 위해 사용
        
        # 반복하면서 홀짝 노드 처리
        while even and even.next:
            odd.next = odd.next.next
            odd = odd.next
            
            even.next = even.next.next
            even = even.next
        
        # 홀수 노드의 마지막을 짝수 헤드로 연결
        odd.next = even_head
        
        return head
    


# 연결 리스트 생성
## 1->2->3->4->5

def createLinkedLists():
    # 노드 생성
    node1 = ListNode(1)
    node2 = ListNode(2)
    node3 = ListNode(3)
    node4 = ListNode(4)
    node5 = ListNode(5)

    # 노드 간 포인터 연결
    node1.next = node2
    node2.next = node3
    node3.next = node4
    node4.next = node5

    # 헤드 노드 지정
    head = node1
    
    return head



# 정답 출력
## 1->3->5->2->4

def printAnswer(answer):    
    while answer is not None:
        if answer.val:
            print(f"{answer.val}", end="")
            
        if answer.next is not None:
            print("->", end="")
            
        answer = answer.next
    
    print("")
    
    
    
printAnswer(Solution().oddEvenList(createLinkedLists()))