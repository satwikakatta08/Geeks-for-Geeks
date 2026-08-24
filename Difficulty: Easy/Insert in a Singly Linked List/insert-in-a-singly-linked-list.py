''' Structure of Linked List Node
class Node:
    def __init__(self, x):
        self.data = x
        self.next = None
'''
class Solution:
    def insertPos(self, head, pos, val):
      # code here
        nn=Node(val)
        if pos==1:
            nn.next=head
            return nn
        curr=head
        for i in range(pos-2):
            if curr is None:
                break
            curr=curr.next
        if curr is not None:
            nn.next=curr.next
            curr.next=nn
        return head