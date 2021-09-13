class Node:
    def __init__(self, item):
        self.item = item
        self.next = None

class Linklist:
    def __init__(self):
        self._head = None

lst = Linklist()
node1 = Node(1)
node2 = Node(2)
node3 = Node(3)
lst._head = node1
node1.next = node2
node2.next = node3

print(lst._head.next.next.item)
