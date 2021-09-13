from typing import Optional
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        carry = 0
        root = n = ListNode(0)
        while l1 or l2 or carry:
            v1 = v2 = 0
            if l1:
               v1 = l1.val
               l1 = l1.next
            if l2:
               v2 = l2.val
               l2 = l2.next
            carry, val = divmod(v1+v2+carry, 10)
            n.next = ListNode(val)
            n = n.next
        return root.next

def testlist(l):
    while(True):
        print(l.val)
        if l.next is not None:
            l = l.next
        else:
            print()
            break

if __name__ == '__main__':
    l1_1 = ListNode(3)
    l1_2 = ListNode(4)
    l1_3 = ListNode(2)
    l1_1.next = l1_2
    l1_2.next = l1_3

    l2_1 = ListNode(4)
    l2_2 = ListNode(6)
    l2_3 = ListNode(5)
    l2_1.next = l2_2
    l2_2.next = l2_3

    solute = Solution().addTwoNumbers(l1_1, l2_1)
    testlist(solute)


