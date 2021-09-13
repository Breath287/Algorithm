from typing import Optional
class Node:
    def __init__(self, x):
        self.x = x
        self.next = None

class Solution:
    def addTwonumlinklist(self, l1: Optional[Node], l2: Optional[Node])->Optional[Node]:
        root = n = Node(0)
        carry = 0
        while l1 or l2 or carry:
            v1 = v2 = 0
            if l1:
                v1 = l1.x
                l1 = l1.next
            if l2:
                v2 = l2.x
                l2 = l2.next
            carry, x = divmod(carry+v1+v2, 10)
            n.next = Node(x)
            n = n.next
        return root.next
