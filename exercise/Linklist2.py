class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class Linklist:
    def __init__(self):
        self._head = None

    def is_empty(self):
        return self._head is None

    def length(self):
        cur = self._head
        count = 0
        while cur is not None:
            count += 1
            cur = cur.next
        return count

    def travel(self):
        cur = self._head
        while cur is not None:
            print(cur.value)
            cur = cur.next

    def add(self, item):
        node = Node(item)
        node.next = self._head
        self._head = node

    def append(self, item):
        node = Node(item)
        if self.is_empty():
            self._head = None
        else:
            cur = self._head
            while cur.next is not None:
                cur = cur.next
            cur.next = node

    def insert(self, index, item):
        node = Node(item)
        cur = self._head
        if index <= 0:
            self.add(item)
        if index >= (self.length() - 1):
            self.append(item)
        else:
            for i in range(index -1):
                cur = cur.next
            node.next = cur.next
            cur.next = node

    def remove(self, item):
        cur = self._head
        pre = None
        while cur is not None:
            if cur.item == item:
                if cur == self._head:
                    self._head = cur.next
                else:
                    pre.next = cur.next
            else:
                pre = cur
                cur = cur.next

    def find(self, item):
        return item in self.travel()

if __name__ == "__main__":
    ll = Linklist()
    print(ll.is_empty())
    print(ll.length())

    for i in range(6):
        ll.append(6)
    print(ll.travel())




