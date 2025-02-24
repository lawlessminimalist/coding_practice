# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        if not head or not head.next:
            return head
        
        currentNode = head # 1
        nextNode = head.next # 2
        while(nextNode):
            tempNode = None
            if head == currentNode: # true
                tempNode = currentNode # 1
                currentNode.next = None # 1.next = none
            else:
                tempNode = currentNode

            currentNode = nextNode # curr = 2
            nextNode = currentNode.next #next = 3
            currentNode.next = tempNode # 2.next = 1
        return currentNode


two = ListNode(2,None)
one = ListNode(1,two)
head = ListNode(0,one)
print(head.val)
print(one.val)
print(two.val)


x = Solution().reverseList(head)
print(x.val)
print(x.next.val)
print(x.next.next.val)