# 19. 역순 연결 리스트 2
## 인덱스 m부터 n까지 역순으로 만들어라




from ListNode import ListNode

# 링크드 리스트 정의
ListNode = ListNode



class Solution:
    
    # 풀이 1. 반복 구조로 노드 뒤집기
    
    def reverseBetween(self, head: ListNode, m: int, n: int):
        # 예외 처리
        if not head or m == n:
            return head
        
        root = start = ListNode(None)
        root.next = head
        
        # start는 m 앞의 값으로 지정
        for _ in range(m - 1):
            start = start.next
            
        # end는 m으로 지정
        end = start.next
        
        # 반복하면서 노드 차례대로 뒤집기
        for _ in range(n - m):
            tmp = start.next
            start.next = end.next
            end.next = end.next.next
            start.next.next = tmp
            
        return root.next
    
    

# 입력: 1->2->3->4->5
inputs = ListNode.createLinkedLists(1, 5)

# 출력: 1->4->3->2->5
ListNode.printLinkedLists(Solution().reverseBetween(inputs, 2, 4))