# 14. 두 정렬 리스트의 병합



# 링크드 리스트 정의

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:

    # 풀이 1. 재귀 구조로 연결

    def mergeTwoLists(self, list1: ListNode, list2: ListNode):
        # list1이 list2 보다 크면 서로 위치 바꿈
        if (not list1) or (list2 and list1.val > list2.val):
            list1, list2 = list2, list1

        if list1:
            list1.next = self.mergeTwoLists(list1.next, list2)

        return list1



# 첫 번째 연결 리스트 생성
## 1->2->4
node1 = ListNode(1)
node2 = ListNode(3)
node3 = ListNode(5)

node1.next = node2
node2.next = node3

list1 = node1



# 두 번째 연결 리스트 생성
## 1->3->4
node4 = ListNode(2)
node5 = ListNode(4)
node6 = ListNode(6)

node4.next = node5
node5.next = node6

list2 = node4



solution = Solution()
answer = solution.mergeTwoLists(list1, list2)



# 정답 출력
## 1->1->2->3->4->4

while answer is not None:
    if answer.val:
        print(f"{answer.val}", end="")
        
    if answer.next is not None:
        print("->", end="")
        
    answer = answer.next