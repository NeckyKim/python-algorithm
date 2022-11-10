# 18. 홀짝 연결 리스트
## 연결 리스트를 홀수 노드 다음에 짝수 노드가 오도록 재구성
## 공간 복잡도: O(1), 시간 복잡도: O(n)



from ListNode import ListNode

# 링크드 리스트 정의
ListNode = ListNode



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
    


# 입력: 1->2->3->4->5
inputs = ListNode.createLinkedLists(1, 5)

# 출력: 1->3->5->2->4    
ListNode.printLinkedLists(Solution().oddEvenList(inputs))