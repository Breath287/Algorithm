class Node:
    def __init__(self, element):
        self.element = element
        self.next = None

class SingleList:
    def __init__(self, node = None):
        self._head = node

    def is_empty(self):
        return self._head == None

    def length(self):
        cur = self._head
        count = 0
        while cur != None:
            count += 1
            cur = cur.next
        return count

    def travel(self):
        cur = self._head
        while cur != None:
            print(cur.element, end =' ')
            cur = cur.next
        print('')

    def append(self, item):
        node = Node(item)
        if self.is_empty():
            self._head = node
        else:
            cur = self._head
            while cur.next != None:
                cur = cur.next
            cur.next = node


    def add(self, item):
        node = Node(item)
        if self.is_empty():
            self._head = node
        else:
            node.next = self._head
            self._head = node

    def insert(self, pos, item):
        node = Node(item)
        count = 0
        cur = self._head
        if pos <= 0:
            self.add(item)
        elif pos > (self.length() - 1):
            self.append(item)
        while count < (pos - 1):
            cur = cur.next
        node.next = cur.next

    def remove(self, item):
        cur = self._head
        pre = None
        while cur != None:
            if cur.element == item:
                if cur == self._head:
                    self._head = cur.next
                else:
                    pre.next = cur.next
                break
            else:
                pre = cur
                cur = cur.next



    def search(self, item):
        cur = self._head
        while cur != None:
            if cur.element == item:
                return True
            else:
                cur = cur.next
        return False

if __name__ == "__main__":
    ll = SingleList()
    print(ll.is_empty())
    print(ll.length())

    ll.append(1)
    ll.append(2)
    ll.append(3)
    ll.append(4)
    ll.append(5)
    print(ll.length())
    ll.travel()

    ll.add(0)
    ll.travel()

    ll.insert(1,1)
    ll.travel()

    ll.insert(1,2)
    ll.travel()

    print(ll.search(5))

    ll.remove(5)
    ll.travel()







