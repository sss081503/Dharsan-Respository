class Node(object):
    def __init__(self, data):
        self.data = data
        self.lchild = None
        self.rchild = None
        # self.parent = None
        # self.visited = False

    def __str__(self):
        s = ''
        return s


class Tree(self):
    def __init__(self):
        self.root = None
        # self.size = 0

    # insert data into a tree
    def insert_node(self, data):
        new_node = Node(data)
        # each node must go in a unique place in the binary search tree

        # insert data into a tree
        if self.root is None:
            self.root = new_node
            return
        else:
            current = self.root
            parent = self.root
            while not (current is None):
                parent = current
                if data < current.data:
                    current = current.lchild
                else:
                    current = current.rchild
            if data < parent.data:
                parent.lchild = new_node
            else:
                parent.rchild = new_node

    # find the node with the smallest value
    def min_node(self):
        current = self.root
        parent = self.root
        while current is not None:
            parent = current
            current = current.lchild
        return parent

    # find the node with the largest value
    def max_node(self):
        current = self.root
        parent = self.root
        while current is not None:
            parent = current
            current = current.rchild
        return parent

    # in order traversal - left, center, right
    def in_order(self, aNode):
        # aNode is a generic node

        if aNode is not None:
            self.in_order(aNode.lchild)
            print(aNode.data)
            self.in_order(aNode.rchild)

    # pre order traversal - center, left, right
    def pre_order(self, aNode):
        if aNode is not None:
            print(aNode.data)
            self.pre_order(aNode.lchild)
            self.pre_order(aNode.rchild)

    # post order traversal - left, right, center
    def post_order(self, aNode):
        if aNode is not None:
            self.post_order(aNode.lchild)
            self.post_order(aNode.rchild)
            print(aNode.data)

    # search for a node with a given data
    def search_node(self, data):
        current = self.root
        while (current is not None) and current.data != data:
            if data < current.data:
                current = current.lchild
            else:
                current = current.rchild
        return current
