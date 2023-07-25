class Node:
    def __init__(self, label, value):
        self.label = label
        self.value = value
        self.lc = None
        self.rc = None


class Tree:
    def __init__(self):
        self.root = None

    # Returns a list of nodes at a given level from left to right

    def get_level(self, level):

        current = self.root
        list1 = []

        self.level1(current, level, list1)
        return list1

    def level1(self, current, level, list1):

        if current != None:
            if level == 0:
                list1.append(current.value)
            else:
                self.level1(current.lc, level - 1, list1)
                self.level1(current.rc, level - 1, list1)
                return
        else:
            return list1

    def depth(self, label):
        current = self.root
        c = 0
        if self.root.label == label:
            return 0, self.root

        while (current != None) and (current.data != label):

            c += 1
            if (label < current.label):
                current = current.lchild


            else:
                current = current.rchild

        if c != 1:
            c += 1
        if current.label == label:

            return c, current
        else:
            return 0, current

    def sum(self, d):
        list2 = self.get_level(d)
        return sum(list2)

    def maxsum(self):
        height = self.height1()
        sums = []
        for i in range(height + 1):
            sums.append(self.sum(i))

        return max(sums)

        # Returns the height of the tree

    def height1(self):
        current = self.root
        return self.helper(current)

    def helper(self, current):
        if current is None:
            return 0
        else:
            return max(self.helper(current.rc), self.helper(current.lc)) + 1


def main():
    # The following is an example

    # Initialize the tree nodes
    n1 = Node("n1", 14)
    n2 = Node("n2", 34)
    n3 = Node("n3", 2)
    n4 = Node("n4", 12)
    n5 = Node("n5", 3)
    n6 = Node("n6", 1)

    # Build the tree
    tree = Tree()
    tree.root = n1
    n1.lc = n2
    n1.rc = n3
    n2.lc = n4
    n2.rc = n5
    n3.rc = n6

    # Validate your code
    print(f'The depth of node "n3" should be 1, and your output is {tree.depth("n3")}')
    print(f'The depth of node "n6" should be 2, and your output is {tree.depth("n4")}')
    print(f'The sum of nodes with depth 2 should be 16, and your output is {tree.sum(2)}')
    print(f'The maximam sum should be 36, which is obtained with d=1, and your output is {tree.maxsum()}')


if __name__ == '__main__':
    main()
