"""
class Node:

    def __init__(self, data):
        self.data = data
        self.next = None
"""
class Solution:
    def insertAtFront(self, head, x):
        #code here
        new_node=Node(x)
        new_node.next=head
        return new_node
