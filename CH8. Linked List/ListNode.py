class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None



    def createLinkedLists(start,end):
        memory = [0 for i in range(end)]

        for i in range(end - start + 1):
            memory[i] = ListNode(start + i)
            
        for i in range(end - start):
            memory[i].next = memory[i + 1]

        head = memory[0]
        
        return head
    
    

    def printLinkedLists(node):
        while node is not None:
            if node.val:
                print(f"{node.val}", end="")

            if node.next is not None:
                print("->", end="")

            node = node.next

        print("")