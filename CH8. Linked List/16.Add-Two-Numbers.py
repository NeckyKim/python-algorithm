# 16. 두 수의 덧셈
## 역순으로 저장된 연결 리스트이 숫자를 더하라



# 링크드 리스트 정의

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    
    # 풀이 1. 자료형 변환
    
    # 연결 리스트를 뒤집기(15번 문제 참고)
    def reverseList(self, head: ListNode):
        node = head
        prev = None
            
        while node:
            next = node.next
            node.next = prev
                             
            prev = node
            node = next
                
        return prev
    
    # 연결 리스트를 리스트로 변환
    def toList(self, node: ListNode):
        temp = []
        
        while node:
            temp.append(node.val)
            node = node.next
            
        return temp
    
    # 리스트를 연결 리스트로 변환
    def toLinkedList(self, result: str):
        prev: ListNode = None
        
        for i in result:
            node = ListNode(i)
            node.next = prev
            prev = node
            
        return node
    
    # 두 연결 리스트의 덧셈
    def addTwoNumbers1(self, linkedList1: ListNode, linkedList2: ListNode):
        # 연결 리스트를 뒤집고 리스트로 변환
        list1 = self.toList(self.reverseList(linkedList1))
        list2 = self.toList(self.reverseList(linkedList2))
        
        # 리스트를 정수로 변환
        number1 = int("".join(str(i) for i in list1))
        number2 = int("".join(str(i) for i in list2))
                                                   
        result = number1 + number2
            
        # 최종 계산 결과를 연결 리스트로 변환
        return self.toLinkedList(str(result))
    
    
    
    # 풀이 2. 전가산기 구현
    
    def addTwoNumbers2(self, list1: ListNode, list2: ListNode):
        root = ListNode(0)
        head = ListNode(0)
        
        carry = 0
        
        while list1 or list2 or carry:
            sum = 0
            
            # 두 입력값의 합 계산
            if list1:
                sum = sum + list1.val
                list1 = list1.next
            
            if list2:
                sum = sum + list2.val
                list2 = list2.next
                
            # 몫과 나머지 계산
            carry, val = divmod(sum + carry, 10)
            head.next = ListNode(val)
            head = head.next
        
        return root.next



# 첫 번째 연결 리스트 생성
## 2->4->3

node1 = ListNode(2)
node2 = ListNode(4)
node3 = ListNode(3)

node1.next = node2
node2.next = node3

list1 = node1



# 두 번째 연결 리스트 생성
## 5->6->4

node4 = ListNode(5)
node5 = ListNode(6)
node6 = ListNode(4)

node4.next = node5
node5.next = node6

list2 = node4



# 정답 출력
## 7->0->8

### 2->4->3는 342
### 5->6->4는 465
### 342 + 465 = 807

def printAnswer(answer):    
    while answer is not None:
        if answer.val:
            print(f"{answer.val}", end="")
            
        if answer.next is not None:
            print("->", end="")
            
        answer = answer.next
    
    print("")



printAnswer(Solution().addTwoNumbers1(list1, list2))
printAnswer(Solution().addTwoNumbers2(list1, list2))