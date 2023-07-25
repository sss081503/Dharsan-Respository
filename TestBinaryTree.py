#  File: TestBinaryTree.py

#  Description: exploring different functions with a binary tree

#  Student Name: Dharsan Selvakumar

#  Student UT EID: ss96967

#  Partner Name:

#  Partner UT EID:

#  Course Name: CS 313E

#  Unique Number: 52535

#  Date Created: 11/14/22

#  Date Last Modified: 11/15/22

import sys


class Node(object):
    # from lecture
    def __init__(self, data):
        self.data = data
        self.lChild = None
        self.rChild = None

    def __str__(self):
        return str(self.data)


class Tree(object):
    # from lecture
    def __init__(self):
        self.root = None

    # from lecture: Insert a node in the tree
    # insert data into a tree
    def insert(self, data):
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
                    current = current.lChild
                else:
                    current = current.rChild
            if data < parent.data:
                parent.lChild = new_node
            else:
                parent.rChild = new_node

    # Returns true if two binary trees are similar
    def is_similar(self, pNode):
        return self.similar_helper(self.root, pNode.root)

    # helper function for is_similar
    def similar_helper(self, nodeA, nodeB):
        if nodeA is not None and nodeB is not None:
            if nodeA.data == nodeB.data:
                # recursive call
                # we want to compare the left branches and right branches of each node of both tree,
                # which requires a recursive call
                return self.similar_helper(nodeA.lChild, nodeB.lChild) and \
                       self.similar_helper(nodeA.rChild, nodeB.rChild)
            else:
                return False
        elif nodeB == nodeA:
            return True
        else:
            return False

    # Returns a list of nodes at a given level from left to right
    def get_level(self, level):
        list1 = []
        return self.level_helper(self.root, level, list1)

    # helper function for get_level
    def level_helper(self, nodeA, levelh, list2):
        if nodeA is not None:
            if levelh == 0:
                # if the level is 0, append the node to the list
                list2.append(nodeA.data)
            else:
                # two separate recursive calls to look at the individual nodes in the left branch and right branch
                self.level_helper(nodeA.lChild, levelh - 1, list2)
                self.level_helper(nodeA.rChild, levelh - 1, list2)
        return list2

    # Returns the height of the tree
    def get_height(self):
        return self.height_helper(self.root)

    # helper function for get_height

    def height_helper(self, nodeA):
        # if there is no node
        if nodeA is None:
            return 0
        else:
            # recursive call
            # we want to find the max height from either the left or right branch
            return 1 + max(self.height_helper(nodeA.lChild), self.height_helper(nodeA.rChild))

    # Returns the number of nodes in the left subtree and
    # the number of nodes in the right subtree and the root
    def num_nodes(self):
        # similar to get_height, we will create a helper function with a recursive call
        return self.nodes_helper(self.root)

    # helper function for num_nodes
    def nodes_helper(self, nodeA):
        if nodeA is None:
            return 0
        else:
            # recursive call to find number of nodes
            # looks at the number of nodes in the left branch and right branch
            return 1 + self.nodes_helper(nodeA.lChild) + self.nodes_helper(nodeA.rChild)


def main():
    # Create three trees - two are the same and the third is different
    line = sys.stdin.readline()
    line = line.strip()
    line = line.split()
    tree1_input = list(map(int, line))  # converts elements into ints
    tree1 = Tree()
    for i in range(len(tree1_input)):
        tree1.insert(tree1_input[i])

    line = sys.stdin.readline()
    line = line.strip()
    line = line.split()
    tree2_input = list(map(int, line))  # converts elements into ints
    tree2 = Tree()
    for j in range(len(tree2_input)):
        tree2.insert(tree2_input[j])

    line = sys.stdin.readline()
    line = line.strip()
    line = line.split()
    tree3_input = list(map(int, line))  # converts elements into ints
    tree3 = Tree()
    for k in range(len(tree3_input)):
        tree3.insert(tree3_input[k])

    # Test your method is_similar()
    print(tree1.is_similar(tree2))
    # Print the various levels of two of the trees that are different
    for i in range(len(tree1_input)):
        print(tree1.get_level(i + 1))

    for i in range(len(tree3_input)):
        print(tree3.get_level(i + 1))

    # Get the height of the two trees that are different
    print(tree1.get_height())
    print(tree3.get_height())

    # Get the total number of nodes a binary search tree
    print(tree1.num_nodes())


if __name__ == "__main__":
    main()
