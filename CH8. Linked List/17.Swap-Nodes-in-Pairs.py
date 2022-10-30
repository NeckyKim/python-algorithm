# 17. 페어이 노드 스왑
## 예) 1->2->3->4를 2->1->4->3d으로 만들어라



# 링크드 리스트 정의

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    
    # 풀이 1. 값만 교환
    
    def swapPairs1(self, head: ListNode):
        cur = head
        
        while cur and cur.next:
            # 값만 교환
            cur.val, cur.next.val = cur.next.val, cur.val
            
            # 2칸을 이동
            cur = cur.next.next
        
        return head
    
    # 풀이 2. 반복 구조로 스왑
    
    def swapPairs2(self, head: ListNode):
        root = prev = ListNode(None)
        
        
        prev.next = head
        
        while head and head.next:
            # b가 a(head)를 가리키도록 할당
            
            temp = head.next
            head.next = temp.next
            temp.next = head
            
            # prev가 b를 가리키도록 할당
            prev.next = temp
            
            # 다음번 비교를 위해 이동
            head = head.next
            prev = prev.next.next
            
        return root.next
    
    # 풀이 3. 재귀 구조로 스왑
    
    def swapPairs3(self, head: ListNode):
        if head and head.next:
            temp = head.next
            
            # 스왑된 값을 리턴 받음
            head.next = self.swapPairs3(temp.next)
            
            temp.next = head
            return temp
        
        return head



# 연결 리스트 생성
# 2->1->4->3

def createLinkedLists():
    node1 = ListNode(1)
    node2 = ListNode(2)
    node3 = ListNode(3)
    node4 = ListNode(4)

    node1.next = node2
    node2.next = node3
    node3.next = node4

    head = node1

    return head


# 정답 출력

def printAnswer(answer):    
    while answer is not None:
        if answer.val:
            print(f"{answer.val}", end="")
            
        if answer.next is not None:
            print("->", end="")
            
        answer = answer.next
    
    print("")



printAnswer(Solution().swapPairs1(createLinkedLists()))
printAnswer(Solution().swapPairs2(createLinkedLists()))
printAnswer(Solution().swapPairs3(createLinkedLists()))