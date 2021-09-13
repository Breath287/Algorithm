class BTree:
    def __init__(self, data=None):
        self.data = data  # current node value
        self.left = None    # left pointer
        self.right = None  # right pointer

    def insertLeft(self, data):
        self.left = BTree(data)
        return self.left

    def insertRight(self, data):
        self.right = BTree(data)
        return self.right

    def show(self):
        print(self.data)


