# 15. 역순 연결 리스트



# 링크드 리스트 정의

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
        
class Solution:
    
    # 풀이 1. 재귀 구조로 뒤집기
    
    def reverseList1(self, head: ListNode):
        def reverse(node: ListNode, prev: ListNode = None):
            if not node:
                return prev
            
            # 다음 노드의 주소를 저장
            next = node.next
            
            # 노드의 포인터를 이전 노드로 연결
            node.next = prev
            
            # 재귀 사용
            return reverse(next, node)
        
        return reverse(head)
    
    # 풀이 2. 반복 구조로 뒤집기
    
    def reverseList2(self, head: ListNode):
        node = head
        prev = None
            
        while node:
            next = node.next    # 다음 노드의 주소를 저장
            node.next = prev    # 노드의 포인터를 이전 노드로 연결
                             
            prev = node         # 이전 노드를 현재 노드로
            node = next         # 현재 노드를 다음 노드로 
                
        return prev



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
## 5->4->3->2->1

def printAnswer(answer):    
    while answer is not None:
        if answer.val:
            print(f"{answer.val}", end="")
            
        if answer.next is not None:
            print("->", end="")
            
        answer = answer.next
    
    print("")
    
    
    
printAnswer(Solution().reverseList1(createLinkedLists()))
printAnswer(Solution().reverseList2(createLinkedLists()))