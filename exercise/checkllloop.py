# check if linklist has a loop
class Node:
    def __init__(self, x):
        self.x = x
        self.next = None

class LinkList:
    def __init__(self, head = None):
        slow = head
        fast = head
        if not head:
            return head
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
            if fast == slow:
                return True
        else:
            return False



