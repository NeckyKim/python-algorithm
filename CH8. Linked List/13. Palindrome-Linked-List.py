# 13. 팰린드롬 연결 리스트



from typing import List

# 링크드 리스트 정의
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def isPalindrome(head: ListNode):
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
    
    
    
node1 = ListNode(1)
node2 = ListNode(2)
node3 = ListNode(2)
node4 = ListNode(1)

node1.next = node2
node2.next = node3
node3.next = node4

head = node1

print(Solution.isPalindrome(head))