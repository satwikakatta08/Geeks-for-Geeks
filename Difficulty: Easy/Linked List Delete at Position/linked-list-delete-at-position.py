''' Structure of Linked List Node
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
'''

class Solution:
    def deleteNode(self, head, x):
        #code here
        if not head:
            return None
        if x==1:
            return head.next
        curr=head
        for i in range(1,x-1):
            if curr is not None:
                curr=curr.next
        if curr is not None and curr.next is not None:
            curr.next=curr.next.next
        return head
            
