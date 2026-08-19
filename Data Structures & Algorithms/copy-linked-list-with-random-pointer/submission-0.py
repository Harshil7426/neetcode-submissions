"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        copy=Node(0)
        dummy=copy
        temp=head
        map={}
        while temp is not None:
            dummy.next=Node(temp.val)
            map[temp]=dummy.next
            temp=temp.next
            dummy=dummy.next

        temp=head
        dummy=copy.next
        while temp is not None:
            # if map[temp.random] is not None
            dummy.random=None if temp.random==None else map[temp.random]
            temp=temp.next
            dummy=dummy.next
        return copy.next

        
        




