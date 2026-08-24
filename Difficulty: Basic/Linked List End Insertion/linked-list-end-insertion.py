'''    
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
'''

class Solution:
    def insertAtEnd(self, head, x):
        #code here 
        nn=Node(x)
        if head is None:
            return Node(x)
        if head.next is None:
            head.next=Node(x)
            return head
        self.insertAtEnd(head.next,x)
        return head
            
        